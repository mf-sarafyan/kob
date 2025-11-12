import logging
import os
from typing import Dict, Any, Optional, List, Union

from langchain.agents import create_agent
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

# Try modern import first, fallback to older import
try:
    from langchain_openai import ChatOpenAI
except ImportError:
    try:
        from langchain_community.chat_models import ChatOpenAI
    except ImportError:
        from langchain.chat_models import ChatOpenAI

from src.settings import CONTENT_DIR, INDEX_DIR
from src.agents.tools import get_graph_tools

# Try to import secrets, fallback to environment variable
try:
    from src.secrets import OPENROUTER_API_KEY
except ImportError:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ToolAugmenterAgent:
    """
    Tool-calling agent that uses available tools to augment context for queries.
    Replaces the three-step structure (search -> expand -> summarize) with a single
    agent that dynamically decides which tools to use.
    """
    
    def __init__(
        self, 
        content_dir: str = CONTENT_DIR,
        index_dir: str = INDEX_DIR,
        model: str = "openai/gpt-4o",
        temperature: float = 0.3,
        max_iterations: int = 15,
        api_key: Optional[str] = None
    ):
        """
        Initialize the tool augmenter agent
        
        :param content_dir: Directory containing content
        :param index_dir: Directory for storing indexes
        :param model: OpenRouter model identifier with tool calling support 
                     (e.g., "openai/gpt-4o", "anthropic/claude-3.5-sonnet", "anthropic/claude-3-opus")
        :param temperature: Sampling temperature
        :param max_iterations: Maximum number of tool calls the agent can make
        :param api_key: OpenRouter API key (defaults to OPENROUTER_API_KEY from secrets or env)
        """
        self.content_dir = content_dir
        self.index_dir = index_dir
        self.model = model
        self.temperature = temperature
        self.max_iterations = max_iterations
        
        # Get API key from parameter, secrets file, or environment variable
        api_key = api_key or OPENROUTER_API_KEY
        if not api_key:
            raise ValueError(
                "OpenRouter API key not found. Please set OPENROUTER_API_KEY in src/secrets.py "
                "or as an environment variable."
            )
        
        # Get all available tools
        self.tools = get_graph_tools()
        
        # Initialize the LLM with OpenRouter
        # OpenRouter uses OpenAI-compatible API, so we use ChatOpenAI with base_url
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature,
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "https://github.com/mf-sarafyan/kob",  
                "X-Title": "KEEPERS Campaign Knowledge Base"  
            }
        )
        
        # Create the system prompt from the prompt template
        system_prompt = self._create_system_prompt()
        
        # Create the agent using create_agent (LangChain 1.0 API)
        # This replaces create_openai_tools_agent + AgentExecutor
        self.agent = create_agent(
            model=self.llm,
            tools=self.tools,
            system_prompt=system_prompt
        )
    
    def _create_system_prompt(self) -> str:
        """
        Create the system prompt for the tool-calling agent
        
        :return: System prompt string
        """
        return (
            "You are an expert knowledge base assistant for a D&D campaign. "
            "Your PRIMARY OBJECTIVE is to answer the user's query as well as possible using ONLY the information from the knowledge base.\n\n"
            
            "CRITICAL REQUIREMENTS:\n"
            "- You MUST ALWAYS search the knowledge base using tools before answering - NEVER rely on general knowledge or assumptions\n"
            "- Answers MUST be specific to THIS campaign. Even if you think you know something about D&D in general, "
            "you must verify it exists in this campaign's knowledge base\n"
            "- If you cannot find information in the knowledge base, clearly state that the information is not available, "
            "rather than making up or inferring answers\n"
            "- Always use tools to search - never skip tool usage because you think you know the answer\n\n"
            
            "Everything you do - every tool you use, every entity you explore, every piece of information you gather - "
            "should be guided by one question: 'Does this help me answer the user's query better?'\n\n"
            
            "Available Tools:\n"
            "- search_entity: Search for entities by name or alias. Returns entity names you can explore further.\n"
            "- entity_details: Get the FULL content and attributes for a specific entity (no truncation). Use this when you need to read the entity's content.\n"
            "- entity_connections: Get all connections (relationships) for a specific entity. Shows which entities are connected and how. Use this to discover related entities.\n"
            "- related_entities: Find entities related to a given entity with detailed relationship information and multi-hop exploration (use with entity names from search results)\n"
            "- vector_search: Perform semantic search across documents. Returns entity names that can be explored just like search_entity results.\n"
            "- graph_search: Explore graph connections for an entity (use with entity names from search results)\n\n"
            
            "Answering Strategy:\n"
            "1. Start by analyzing the query: What exactly is the user asking? What information is needed to answer it completely?\n"
            "2. ALWAYS begin by searching the knowledge base:\n"
            "   - Use search_entity to look for entities mentioned in the query by name or alias\n"
            "   - If search_entity doesn't find results, IMMEDIATELY try vector_search with the query or entity name\n"
            "   - vector_search returns entity names in the same format as search_entity - you can explore these entities using entity_details, entity_connections, related_entities, or graph_search\n"
            "   - Never skip searching - always verify information exists in the knowledge base\n"
            "3. When you find entities (from either search_entity or vector_search), explore them:\n"
            "   - Use entity_details when you need to read the FULL content of an entity (no truncation)\n"
            "   - Use entity_connections to see what other entities are connected and explore relationships\n"
            "   - When entity_connections shows connected entities, check if those connections are relevant to the query\n"
            "   - You can use the connected entity names directly with entity_details, entity_connections, related_entities, or graph_search\n"
            "   - Use related_entities when you need deeper multi-hop relationship exploration\n"
            "   - Use graph_search for more advanced graph traversal\n"
            "4. Before exploring further, ask yourself: 'Do I have enough information to answer the query well?'\n"
            "5. If the answer is incomplete, identify what's missing and explore entities that will fill those gaps\n"
            "6. Synthesize all gathered information into a direct, comprehensive answer to the user's query\n"
            "7. Your final output should be a clear, well-structured answer to the query - not a summary of information gathered\n"
            "8. If you cannot find sufficient information in the knowledge base, explicitly state what information is missing\n\n"
            
            "Handling Relationship Queries:\n"
            "When a query describes a relationship (e.g., \"What is the name of King Arthur's sword?\", \"Where is Luigi's bar?\", \"Who commands the Keepers?\"), do not search for the entire composed phrase.\n\n"
            
            "Instead, follow these steps:\n"
            "1. Identify the explicit entities mentioned in the query (here: King Arthur, Luigi, the Keepers)\n"
            "2. Locate those entities first using search_entity or vector_search\n"
            "3. Once found, explore their connections with entity_connections, related_entities, or graph_search to uncover the linked entities that satisfy the relationship (e.g., \"owns\", \"wields\", \"commands\", \"operates in\", \"member of\")\n"
            "4. Retrieve the details of the connected entity (via entity_details) to answer the question\n\n"
            
            "CRITICAL: Never assume or fabricate a combined entity name like \"King Arthur's sword\" or \"Luigi's bar\" unless you have already discovered that exact title or alias within the knowledge base.\n\n"
            
            "Graph Exploration Strategy:\n"
            "The knowledge graph contains connections between entities. Explore these connections ONLY when they help you answer the query better.\n\n"
            
            "Explore related entities when:\n"
            "- The query explicitly asks about relationships, connections, or interactions\n"
            "- The query requires context that related entities provide (e.g., 'Who are the Keepers?' → explore members, organizations, events)\n"
            "- Your current answer is incomplete because you're missing information about connected entities\n"
            "- The query is about a topic that inherently involves relationships (e.g., political structures, organizations, family histories)\n\n"
            "- You're not entirely sure about the answer to the query, but you think you can find more information with the related entities tool\n\n"
            
            "Do NOT explore blindly:\n"
            "- Don't explore entities just because they're connected - only explore if they're relevant to the query\n"
            "- Don't explore multiple hops away unless those distant connections are necessary to answer the query\n"
            "- If you have enough information to answer the query well, stop exploring and provide your answer\n"
            "- Each tool call should have a clear purpose: gathering specific information needed to answer the query\n\n"
            
            "Answer Quality:\n"
            "- Your answer should directly address what the user asked\n"
            "- Be comprehensive but focused - include all relevant information, exclude irrelevant details\n"
            "- Structure your answer clearly and logically\n"
            "- Base your answer ONLY on information retrieved from the knowledge base - never make up information\n"
            "- If information is missing or incomplete, acknowledge it in your answer\n"
            "- When multiple sources provide information, synthesize them into a coherent answer\n"
            "- Be specific to this campaign - avoid generic D&D knowledge unless verified in the knowledge base\n\n"
            
            "Remember: Your goal is to answer the query as well as possible using ONLY information from the knowledge base. "
            "Every tool use should serve this goal. Always search before answering."
        )
    
    def __call__(self, query: str, chat_history: Optional[List[BaseMessage]] = None) -> Dict[str, Any]:
        """
        Augment context for a query using tool-calling agent
        
        :param query: User query to augment
        :param chat_history: Optional list of previous messages (BaseMessage objects) for conversation context
        :return: Comprehensive context and response
        """
        try:
            logger.info(f"Processing query: {query}")
            
            # Prepare messages for LangChain 1.0 agent format
            messages = []
            
            # Add chat history if provided
            if chat_history:
                # Convert BaseMessage objects to dict format if needed
                for msg in chat_history:
                    if isinstance(msg, dict):
                        messages.append(msg)
                    elif hasattr(msg, 'content'):
                        # Convert BaseMessage to dict format
                        role = "user" if isinstance(msg, HumanMessage) else ("assistant" if isinstance(msg, AIMessage) else "user")
                        messages.append({"role": role, "content": msg.content})
                    else:
                        # Fallback: try to convert to string
                        messages.append({"role": "user", "content": str(msg)})
                logger.info(f"Using chat history with {len(chat_history)} messages")
            
            # Add the current query
            messages.append({"role": "user", "content": query})
            
            # Invoke the agent with the messages format
            result = self.agent.invoke({"messages": messages})
            
            # Extract the final answer from the result
            # In LangChain 1.0, the result is typically a dict with "messages" key
            # The last message should be the AI's response
            if isinstance(result, dict) and "messages" in result:
                messages_result = result["messages"]
                if messages_result and len(messages_result) > 0:
                    # Get the last message which should be the AI response
                    last_message = messages_result[-1]
                    if hasattr(last_message, 'content'):
                        final_answer = last_message.content
                    elif isinstance(last_message, dict):
                        final_answer = last_message.get("content", "")
                    else:
                        final_answer = str(last_message)
                else:
                    final_answer = ""
            elif isinstance(result, dict) and "output" in result:
                final_answer = result["output"]
            else:
                # Fallback: try to extract content from result
                final_answer = str(result)
            
            # Extract intermediate steps if available
            # In LangChain 1.0, intermediate steps might be in the messages or a separate key
            intermediate_steps = []
            if isinstance(result, dict):
                if "intermediate_steps" in result:
                    intermediate_steps = result["intermediate_steps"]
                elif "messages" in result:
                    # Try to extract tool calls from messages
                    for msg in result["messages"]:
                        if hasattr(msg, 'tool_calls') and msg.tool_calls:
                            intermediate_steps.extend(msg.tool_calls)
            
            # Format the result similar to context_augmenter output
            formatted_result = {
                "query": query,
                "answer": final_answer,
                "tool_calls": self._format_tool_calls(intermediate_steps),
                "success": True
            }
            
            logger.info(f"Query processed successfully")
            return formatted_result
            
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            return {
                "query": query,
                "answer": f"Error processing query: {str(e)}",
                "tool_calls": [],
                "success": False,
                "error": str(e)
            }
    
    def _format_tool_calls(self, intermediate_steps: List) -> List[Dict[str, Any]]:
        """
        Format intermediate steps into a readable structure
        
        :param intermediate_steps: List of (tool_call, result) tuples
        :return: List of formatted tool call dictionaries
        """
        formatted_calls = []
        
        for step in intermediate_steps:
            if len(step) >= 2:
                tool_call, result = step[0], step[1]
                
                # Handle both dict-like and object-like tool calls
                # ToolAgentAction objects have .tool and .tool_input attributes
                if hasattr(tool_call, 'tool'):
                    tool_name = tool_call.tool
                    tool_input = getattr(tool_call, 'tool_input', {})
                elif isinstance(tool_call, dict):
                    tool_name = tool_call.get("tool", "unknown")
                    tool_input = tool_call.get("tool_input", {})
                else:
                    # Fallback: try to convert to string or use unknown
                    tool_name = str(tool_call) if tool_call else "unknown"
                    tool_input = {}
                
                tool_info = {
                    "tool": tool_name,
                    "tool_input": tool_input,
                    "result": str(result)[:500] if result else ""  # Truncate long results
                }
                
                formatted_calls.append(tool_info)
        
        return formatted_calls
    
    def stream(self, query: str):
        """
        Stream responses from the agent (for real-time updates)
        
        :param query: User query
        :yield: Streaming chunks of the response
        """
        try:
            for chunk in self.agent.stream({"messages": [{"role": "user", "content": query}]}):
                yield chunk
        except Exception as e:
            logger.error(f"Error streaming response: {e}")
            yield {"error": str(e)}


def create_tool_augmenter(
    content_dir: str = CONTENT_DIR, 
    index_dir: str = INDEX_DIR,
    model: str = "openai/gpt-4o",
    temperature: float = 0.3,
    max_iterations: int = 15,
    api_key: Optional[str] = None
) -> ToolAugmenterAgent:
    """
    Create a tool augmentation agent using OpenRouter
    
    :param content_dir: Directory containing content
    :param index_dir: Directory for storing indexes
    :param model: OpenRouter model identifier with tool calling support
                 (e.g., "openai/gpt-4o", "anthropic/claude-3.5-sonnet", "anthropic/claude-3-opus")
    :param temperature: Sampling temperature
    :param max_iterations: Maximum number of tool calls
    :param api_key: OpenRouter API key (defaults to OPENROUTER_API_KEY from secrets or env)
    :return: Configured ToolAugmenterAgent
    """
    return ToolAugmenterAgent(
        content_dir=content_dir,
        index_dir=index_dir,
        model=model,
        temperature=temperature,
        max_iterations=max_iterations,
        api_key=api_key
    )


# Main execution for testing
if __name__ == '__main__':
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description='Tool Augmenter Test Tool')
    parser.add_argument('--debug', action='store_true', 
                        help='Print full JSON output')
    parser.add_argument('--query', type=str, required=True,
                        help='Query to test')
    args = parser.parse_args()
    
    # Create tool augmenter
    tool_augmenter = create_tool_augmenter()
    
    # Run augmentation for the query
    print(f"\n{'='*60}")
    print(f"Query: {args.query}")
    print('='*60)
    
    result = tool_augmenter(args.query)
    
    # Print answer
    if result.get('answer'):
        print("\nAnswer:")
        print(result['answer'])
    
    # Print tool calls summary
    if result.get('tool_calls'):
        print(f"\nTool Calls ({len(result['tool_calls'])}):")
        for i, call in enumerate(result['tool_calls'], 1):
            print(f"  {i}. {call['tool']}")
            if call.get('tool_input'):
                print(f"     Input: {call['tool_input']}")
    
    # If debug flag is set, print full JSON
    if args.debug:
        print("\nFull Result:")
        print(json.dumps(result, indent=2, default=str))

