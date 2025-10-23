import os
import logging
import json
from typing import List, Dict, Any, Optional

from langchain.agents import AgentExecutor, Tool, ZeroShotAgent
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.schema import AgentAction, AgentFinish

from src.settings import CONTENT_DIR, INDEX_DIR, LLM_MODEL
from src.rag import (
    create_rag_index, 
    create_search_tools
)

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ContextAugmenterAgent:
    """
    An agent that uses vector and graph search to augment context for query resolution
    with a strict JSON response format
    """
    
    def __init__(
        self, 
        llm: Optional[ChatOllama] = None,
        content_dir: str = CONTENT_DIR,
        index_dir: str = INDEX_DIR,
        model: str = LLM_MODEL
    ):
        """
        Initialize the context augmenter agent
        
        :param llm: Language model to use (defaults to Ollama)
        :param content_dir: Directory containing content
        :param index_dir: Directory for storing indexes
        :param model: Specific model to use (defaults to settings.LLM_MODEL)
        """
        # Create RAG index
        self.vector_store, self.graph_builder, _ = create_rag_index(
            content_dir, 
            index_dir
        )
        
        # Create search tools
        self.vector_search_tool, self.graph_search_tool = create_search_tools(
            self.vector_store, 
            self.graph_builder
        )
        
        # Initialize LLM with GPU memory management
        try:
            self.llm = llm or ChatOllama(
                model=model,
                num_gpu=1,
                num_ctx=1024,  # Reduced context window
                temperature=0.0,  # Most deterministic setting
                options={
                    'numa': False,
                    'stop': ['\n\n'],
                    'gpu_layers': 16,
                }
            )
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            # Fallback to CPU mode
            try:
                self.llm = llm or ChatOllama(
                    model=model,
                    num_gpu=0,
                    num_ctx=1024,
                    temperature=0.0
                )
            except Exception as cpu_error:
                logger.error(f"Failed to initialize LLM in CPU mode: {cpu_error}")
                raise RuntimeError(f"Could not initialize language model: {cpu_error}")
        
        # Modify tools to be more explicit
        self.tools = [
            Tool(
                name="Vector Search",
                func=self.vector_search_tool._run,
                description=(
                    "STRICT: Semantic search for multi-word, content-based queries. "
                    "ONLY use for queries longer than one word. "
                    "RETURN RAW SEARCH RESULTS ONLY."
                )
            ),
            Tool(
                name="Graph Search", 
                func=self.graph_search_tool._run,
                description=(
                    "STRICT: Entity relationship search. "
                    "ONLY use for SINGLE ENTITY exact matches. "
                    "RETURN RAW GRAPH RESULTS ONLY."
                )
            )
        ]
        
        # Prepare prompt template for JSON response
        self.prompt = PromptTemplate(
            template=(
                "You are a precise context retrieval agent with ONE SOLE PURPOSE: "
                "Execute the appropriate search tools to gather ONLY relevant information.\n\n"
                "STRICT INSTRUCTIONS:\n"
                "1. ALWAYS return a VALID JSON response\n"
                "2. ONLY use the provided tools to retrieve information\n"
                "3. Strictly follow this JSON structure:\n"
                "{\n"
                "  'query': 'ORIGINAL_QUERY',\n"
                "  'search_results': [\n"
                "    {\n"
                "      'tool_name': 'Vector Search or Graph Search',\n"
                "      'results': ['result1', 'result2', ...]\n"
                "    }\n"
                "  ],\n"
                "  'tools_used': ['Vector Search', 'Graph Search'],\n"
                "  'error': null\n"
                "}\n\n"
                "User Query: {input}\n\n"
                "TOOL SELECTION RULES:\n"
                "- Use Vector Search for content-based, multi-word queries\n"
                "- Use Graph Search ONLY for single-entity, exact-match queries\n\n"
                "Observation:"
            ),
            input_variables=["input"]
        )
        
        # Create agent chain
        self.llm_chain = LLMChain(
            llm=self.llm, 
            prompt=self.prompt
        )
        
        # Create agent executor
        self.agent_executor = AgentExecutor.from_agent_and_tools(
            agent=ZeroShotAgent(
                llm_chain=self.llm_chain, 
                tools=self.tools,
                verbose=True
            ),
            tools=self.tools,
            verbose=True,
            max_iterations=5
        )
    
    def augment_context(self, query: str) -> Dict[str, Any]:
        """
        Augment context for a given query with a strict JSON response
        
        :param query: User query to augment
        :return: Dictionary with context and reasoning in a structured JSON format
        """
        try:
            # Run agent executor
            response = self.agent_executor.run(query)
            
            # Attempt to parse the response as JSON
            try:
                parsed_response = json.loads(response)
                
                # Validate the JSON structure
                if not all(key in parsed_response for key in ['query', 'search_results', 'tools_used', 'error']):
                    raise ValueError("Invalid JSON structure")
                
                return parsed_response
            
            except (json.JSONDecodeError, ValueError) as json_error:
                # Fallback to a structured error response
                logger.error(f"JSON parsing error: {json_error}")
                return {
                    'query': query,
                    'search_results': [],
                    'tools_used': [tool.name for tool in self.tools],
                    'error': f"Failed to parse JSON response: {str(json_error)}"
                }
        
        except Exception as e:
            logger.error(f"Context augmentation error: {e}")
            return {
                'query': query,
                'search_results': [],
                'tools_used': [tool.name for tool in self.tools],
                'error': str(e)
            }
    
    def __call__(self, query: str) -> Dict[str, Any]:
        """
        Alias for augment_context
        
        :param query: User query to augment
        :return: Augmented context in JSON format
        """
        return self.augment_context(query)

# Example usage
def create_context_augmenter(
    content_dir: str = CONTENT_DIR, 
    index_dir: str = INDEX_DIR,
    model: str = LLM_MODEL
) -> ContextAugmenterAgent:
    """
    Create a context augmentation agent
    
    :param content_dir: Directory containing content
    :param index_dir: Directory for storing indexes
    :param model: Specific model to use (defaults to settings.LLM_MODEL)
    :return: Configured ContextAugmenterAgent
    """
    return ContextAugmenterAgent(
        content_dir=content_dir, 
        index_dir=index_dir,
        model=model
    )

# Main execution for testing
if __name__ == '__main__':
    # Create context augmenter
    context_augmenter = create_context_augmenter()
    
    # Test queries
    test_queries = [
        "Rock of Bral political structure",  # Multi-word vector search
        "Baang",  # Single-entity graph search
        "Keepers faction relationships",  # Multi-word vector search
        "Vax",  # Single-entity graph search
        "campaign current events"  # Multi-word vector search
    ]
    
    # Run augmentation for each query
    for query in test_queries:
        print(f"\n=== Query: {query} ===")
        result = context_augmenter(query)
        print(json.dumps(result, indent=2))
