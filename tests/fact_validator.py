"""
Counter-factual validator that checks if facts mentioned in the assistant response
are supported by the context retrieved from tool calls.
"""

import logging
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Try modern import first, fallback to older import
try:
    from langchain_openai import ChatOpenAI
except ImportError:
    try:
        from langchain_community.chat_models import ChatOpenAI
    except ImportError:
        from langchain.chat_models import ChatOpenAI

# Try to import secrets, fallback to environment variable
import os
try:
    from src.secrets import OPENROUTER_API_KEY
except ImportError:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

logger = logging.getLogger(__name__)


class FactValidationResult(BaseModel):
    """
    Pydantic model for fact validation results.
    This ensures structured output from the LLM.
    """
    supported_facts: List[str] = Field(
        default_factory=list,
        description="List of facts from the response that ARE supported by the context"
    )
    unsupported_facts: List[str] = Field(
        default_factory=list,
        description="List of facts from the response that are NOT supported by the context"
    )
    summary: str = Field(
        default="",
        description="A brief summary of the validation results"
    )
    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Overall confidence score (0.0 to 1.0) indicating that the response is factually accurate based on the context"
    )


class FactValidator:
    """
    Validates that facts in the assistant response are supported by the context.
    Uses an LLM to perform counter-factual checking.
    """
    
    def __init__(
        self,
        model: str = "openai/gpt-4o",
        temperature: float = 0.0,
        api_key: Optional[str] = None
    ):
        """
        Initialize the fact validator.
        
        :param model: OpenRouter model identifier
        :param temperature: Sampling temperature (use 0.0 for deterministic fact-checking)
        :param api_key: OpenRouter API key
        """
        self.model = model
        self.temperature = temperature
        
        # Get API key
        api_key = api_key or OPENROUTER_API_KEY
        if not api_key:
            raise ValueError(
                "OpenRouter API key not found. Please set OPENROUTER_API_KEY in src/secrets.py "
                "or as an environment variable."
            )
        
        # Initialize the LLM
        llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "https://github.com/mf-sarafyan/kob",
                "X-Title": "KEEPERS Campaign Knowledge Base - Fact Validator"
            }
        )
        
        # Create JSON output parser with Pydantic model
        # This ensures structured output matching our schema
        self.json_parser = JsonOutputParser(pydantic_object=FactValidationResult)
        
        # Create the validation prompt (needs parser for format instructions)
        self.prompt = self._create_validation_prompt()
        
        # Create the chain: prompt -> LLM -> JSON parser -> Pydantic model
        # This gives us programmatic schema validation while working with OpenRouter
        self.chain = self.prompt | llm | self.json_parser
    
    def _create_validation_prompt(self) -> ChatPromptTemplate:
        """Create the prompt template for fact validation."""
        return ChatPromptTemplate.from_messages([
            ("system",
             "You are a fact-checker for a D&D campaign knowledge base assistant. "
             "Your task is to analyze whether the facts mentioned in an assistant's response "
             "are actually supported by the context that was retrieved from the knowledge base.\n\n"
             
             "CRITICAL REQUIREMENTS:\n"
             "- You must be STRICT: Only facts that are explicitly stated or clearly inferable "
             "from the context should be marked as supported\n"
             "- If a fact is mentioned in the response but NOT found in the context, it is "
             "UNSUPPORTED (the assistant may have made it up or used general knowledge)\n"
             "- If a fact is partially supported but details are wrong, mark it as UNSUPPORTED\n"
             "- Be precise: distinguish between what is actually in the context vs. what the "
             "assistant might be inferring or making up\n\n"
             
             "You will receive:\n"
             "1. The original query\n"
             "2. The assistant's response\n"
             "3. The context retrieved from tool calls (entity details, search results, etc.)\n\n"
             
             "Analyze the facts in the assistant response and determine which are supported by the context. "
             "Return a structured JSON response with supported facts, unsupported facts, a summary, and a confidence score.\n\n"
             
             "{format_instructions}"
            ),
            ("human", 
             "Query: {query}\n\n"
             "Assistant Response:\n{response}\n\n"
             "Retrieved Context:\n{context}\n\n"
             "Analyze the facts in the assistant response and determine which are supported by the context."
            )
        ]).partial(format_instructions=self.json_parser.get_format_instructions())
    
    def _extract_context_from_tool_calls(self, tool_calls: List[Dict[str, Any]]) -> str:
        """
        Extract and format context from tool call results.
        
        :param tool_calls: List of tool call dictionaries with 'tool', 'tool_input', 'result'
        :return: Formatted context string
        """
        context_parts = []
         
        for i, call in enumerate(tool_calls, 1):
            tool_name = call.get('tool', 'unknown')
            tool_input = call.get('tool_input', {})
            result = call.get('result', '')
            
            context_parts.append(f"--- Tool Call {i}: {tool_name} ---")
            if tool_input:
                # Format tool input nicely
                if isinstance(tool_input, dict):
                    input_str = ", ".join([f"{k}={v}" for k, v in tool_input.items()])
                else:
                    input_str = str(tool_input)
                context_parts.append(f"Input: {input_str}")
            
            # Include the full result (truncate if extremely long, but keep most of it)
            if result:
                result_str = str(result)
                # Keep up to 2000 chars per tool result to avoid token limits
                if len(result_str) > 2000:
                    result_str = result_str[:2000] + "... [truncated]"
                context_parts.append(f"Result:\n{result_str}")
            
            context_parts.append("")  # Empty line between tool calls
        
        return "\n".join(context_parts)
    
    def validate(
        self,
        query: str,
        response: str,
        tool_calls: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Validate that facts in the response are supported by the context.
        
        :param query: Original user query
        :param response: Assistant's response
        :param tool_calls: List of tool calls with their results
        :return: Validation results dictionary
        """
        try:
            # Extract context from tool calls
            context = self._extract_context_from_tool_calls(tool_calls)
            
            if not context.strip():
                logger.warning("No context extracted from tool calls")
                return {
                    "supported_facts": [],
                    "unsupported_facts": [],
                    "summary": "No context available for validation",
                    "confidence": 0.0,
                    "error": "No context extracted from tool calls"
                }
            
            # Invoke the chain for validation with structured output
            # The chain returns a FactValidationResult Pydantic model
            validation_result = self.chain.invoke({
                "query": query,
                "response": response,
                "context": context
            })
            
            # Convert Pydantic model to dict for consistency with return type
            return {
                "supported_facts": validation_result.supported_facts,
                "unsupported_facts": validation_result.unsupported_facts,
                "summary": validation_result.summary,
                "confidence": validation_result.confidence
            }
            
        except Exception as e:
            logger.error(f"Error during fact validation: {e}")
            return {
                "supported_facts": [],
                "unsupported_facts": [],
                "summary": f"Validation error: {str(e)}",
                "confidence": 0.0,
                "error": str(e)
            }

