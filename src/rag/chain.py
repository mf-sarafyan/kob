import os
import time
import logging
from typing import Dict, List, Any, Optional, Type
import functools
import signal
import threading
import queue

import networkx as nx
import json

from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableMap
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from .graph import ObsidianGraphBuilder
from src.settings import CONTENT_DIR

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Cross-platform timeout decorator using threading
def timeout(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Queue to store result or exception
            result_queue = queue.Queue()
            
            # Thread function to run the original function
            def worker():
                try:
                    result = func(*args, **kwargs)
                    result_queue.put(result)
                except Exception as e:
                    result_queue.put(e)
            
            # Start the thread
            thread = threading.Thread(target=worker)
            thread.daemon = True  # Allows thread to be killed when main thread exits
            thread.start()
            
            # Wait for the specified timeout
            thread.join(timeout=seconds)
            
            # Check if thread is still alive (timed out)
            if thread.is_alive():
                raise TimeoutError(f"Function {func.__name__} timed out after {seconds} seconds")
            
            # Retrieve the result or re-raise any exception
            result = result_queue.get()
            if isinstance(result, Exception):
                raise result
            
            return result
        return wrapper
    return decorator

def create_graph_retriever(graph_path: str):
    """
    Create a graph-based retriever from a pre-built graph
    
    :param graph_path: Path to the exported graph JSON
    :return: NetworkX graph object
    """
    with open(graph_path, 'r', encoding='utf-8') as f:
        graph_data = json.load(f)
    
    return nx.readwrite.json_graph.node_link_graph(graph_data)

def graph_enhanced_retrieval(graph: nx.MultiDiGraph, query: str, vector_store, top_k: int = 4) -> List[Dict[str, Any]]:
    """
    Enhance vector retrieval with graph-based context
    
    :param graph: NetworkX graph
    :param query: User query
    :param vector_store: Existing vector store
    :param top_k: Number of documents to retrieve
    :return: List of enhanced documents
    """
    # First, get vector-based retrieval results
    vector_docs = vector_store.similarity_search(query, k=top_k)
    
    # Enhance documents with graph context
    enhanced_docs = []
    for doc in vector_docs:
        # Try to find the node in the graph
        node_name = os.path.splitext(os.path.basename(doc.metadata.get('source', '')))[0]
        
        # Get graph context if node exists
        graph_context = {}
        if node_name in graph.nodes:
            graph_context = {
                'direct_connections': list(graph.neighbors(node_name)),
                'node_type': graph.nodes[node_name].get('type', 'unknown')
            }
        
        # Create enhanced document
        enhanced_doc = doc.copy()
        enhanced_doc.metadata['graph_context'] = graph_context
        enhanced_docs.append(enhanced_doc)
    
    return enhanced_docs

def extract_entities(query: str, graph: nx.MultiDiGraph, top_n: int = 3) -> List[str]:
    """
    Extract potential entities from a query
    
    :param query: User query
    :param graph: NetworkX graph
    :param top_n: Number of entities to return
    :return: List of most relevant entities
    """
    logger.info(f"Extracting entities for query: {query}")
    
    # Get all nodes
    all_nodes = list(graph.nodes())
    
    # Score entities based on query similarity
    query_words = set(query.lower().split())
    
    # Score entities
    entity_scores = []
    for node in all_nodes:
        # Normalize node name
        node_lower = node.lower()
        
        # Calculate score based on word overlap
        score = len(set(node_lower.split()) & query_words)
        
        # Bonus for exact matches
        if node_lower in query.lower():
            score += 2
        
        entity_scores.append((node, score))
    
    # Sort and return top entities
    top_entities = [
        entity for entity, score in 
        sorted(entity_scores, key=lambda x: x[1], reverse=True)[:top_n]
        if score > 0
    ]
    
    logger.info(f"Top entities: {top_entities}")
    return top_entities

@timeout(30)  # 30-second timeout
def expand_entity_context(
    entity: str, 
    graph_builder: ObsidianGraphBuilder, 
    max_depth: int = 2
) -> str:
    """
    Expand context for a given entity
    
    :param entity: Entity name to explore
    :param graph_builder: Graph builder instance
    :param max_depth: Maximum depth of context exploration
    :return: Formatted context string
    """
    logger.info(f"Expanding context for entity: {entity}")
    start_time = time.time()
    
    try:
        # Get comprehensive entity context
        context = graph_builder.expand_context(entity, max_depth=max_depth)
        
        # Format context for LLM
        context_str = f"Context for {entity}:\n"
        
        # Add node details
        context_str += "Node Details:\n"
        for key, value in context['node_data'].items():
            if value:  # Only add non-empty values
                context_str += f"- {key}: {value}\n"
        
        # Add direct connections
        context_str += "\nDirect Connections:\n"
        for conn_name, conn_details in context['connections']['direct'].items():
            context_str += (
                f"- {conn_name} (Type: {conn_details['type']}, "
                f"Weight: {conn_details['weight']:.2f})\n"
            )
        
        # Add related entities
        if context.get('related_entities'):
            context_str += "\nRelated Entities:\n"
            for rel_name, rel_details in context['related_entities'].items():
                context_str += (
                    f"- {rel_name} (Connection: {rel_details['connection']['relationship_type']}, "
                    f"Weight: {rel_details['connection']['weight']:.2f})\n"
                )
        
        logger.info(f"Context expansion for {entity} took {time.time() - start_time:.2f} seconds")
        return context_str
    
    except TimeoutError:
        logger.warning(f"Context expansion for {entity} timed out")
        return f"Timeout expanding context for {entity}"
    except Exception as e:
        logger.error(f"Error expanding context for {entity}: {e}")
        return f"Error expanding context for {entity}: {e}"

def extract_potential_entities(query: str, graph: nx.MultiDiGraph) -> List[str]:
    """
    Extract potential entities from a query without strict scoring
    
    :param query: User query
    :param graph: NetworkX graph
    :return: List of potential entity names
    """
    # Normalize query words
    query_words = set(query.lower().split())
    
    # Find nodes that have words matching query
    potential_entities = []
    for node in graph.nodes():
        # Convert node to lowercase for case-insensitive matching
        node_lower = node.lower()
        
        # Check if any query word is in the node name
        if any(word in node_lower for word in query_words):
            potential_entities.append(node)
    
    return potential_entities

def generate_graph_exploration_prompt(
    query: str, 
    initial_context: str, 
    graph: nx.MultiDiGraph
) -> str:
    """
    Generate a prompt that guides the LLM to explore the graph if needed
    
    :param query: Original user query
    :param initial_context: Context from initial vector search
    :param graph: NetworkX graph
    :return: Exploration guidance prompt
    """
    # Extract potential entities
    potential_entities = extract_potential_entities(query, graph)
    
    # Construct exploration guidance
    exploration_prompt = f"""
    Graph Exploration Guidance:
    
    You have access to a knowledge graph representing the campaign's entities and their relationships.
    
    Initial Context Evaluation:
    1. Carefully assess the initial context: 
    {initial_context[:500]}...
    
    2. Determine if this context fully answers the query "{query}".
    
    3. If the context seems incomplete, you MAY explore related entities:
    Potential Related Entities: {potential_entities[:5]}
    
    Graph Exploration Instructions:
    - You can request additional context about related entities
    - Use the graph to find connections between entities
    - Focus on entities that might provide meaningful additional information
    - Be judicious - only explore if you believe it will significantly improve the answer
    
    Exploration Request Format (if needed):
    - Specify EXACTLY which entity's context you want to explore
    - Explain briefly WHY this entity's context is relevant
    
    Example Exploration Request:
    "Explore context for 'Bral' to understand the political landscape relevant to the query."
    
    Decision Guidelines:
    - Prioritize conciseness
    - Only explore if initial context is genuinely insufficient
    - Your goal is to provide the most accurate and helpful response
    """
    
    return exploration_prompt

def make_graph_rag_chain(
    vector_store, 
    graph_path: str, 
    llm_model: str, 
    top_k: int = 4
):
    """
    Create a graph-enhanced RAG chain with LLM-driven context exploration
    
    :param vector_store: Existing vector store
    :param graph_path: Path to the exported graph JSON
    :param llm_model: Language model to use
    :param top_k: Number of documents to retrieve
    :return: Langchain RAG chain
    """
    logger.info("Creating graph-enhanced RAG chain")
    
    # Load graph
    graph = nx.readwrite.json_graph.node_link_graph(
        json.load(open(graph_path, 'r', encoding='utf-8'))
    )
    
    # Initialize graph builder
    graph_builder = ObsidianGraphBuilder(os.path.dirname(graph_path))
    graph_builder.graph = graph
    
    # Create graph exploration tool
    graph_exploration_tool = create_graph_exploration_tool(graph_builder)
    
    # LLM
    llm = ChatOllama(model=llm_model)
    
    # Retrieval function
    def retrieve_with_graph(query):
        logger.info(f"Retrieving context for query: {query}")
        
        # First, get vector-based retrieval results
        vector_docs = vector_store.similarity_search(query, k=top_k)
        
        return vector_docs
    
    # Prompt template with graph exploration guidance
    prompt_template = PromptTemplate.from_template("""
    You are an expert assistant for a D&D campaign. 
    
    Initial Context:
    {context}
    
    {graph_exploration_guidance}
    
    Query: {query}
    
    Response Guidelines:
    1. Use the initial context as your primary source of information
    2. If the context is insufficient, explain what additional information you need
    3. Be precise, concise, and helpful
    4. If you request graph exploration, clearly state WHY and use the graph_exploration_tool
    5. You have access to a graph_exploration_tool to retrieve additional context
    
    Available Tools:
    - graph_exploration_tool: Explore detailed context of a specific entity
    """)
    
    # Construct the RAG chain
    def rag_with_sources(inputs):
        logger.info(f"Processing query: {inputs['query']}")
        
        try:
            # Retrieve initial documents
            docs = retrieve_with_graph(inputs["query"])
            
            # Prepare initial context
            context = "\n\n".join(doc.page_content for doc in docs)
            
            # Generate graph exploration guidance
            graph_exploration_guidance = generate_graph_exploration_prompt(
                inputs["query"], 
                context, 
                graph
            )
            
            # Prepare input for the chain
            chain_input = {
                "context": context,
                "graph_exploration_guidance": graph_exploration_guidance,
                "query": inputs["query"]
            }
            
            # Run the chain
            result = (
                prompt_template 
                | llm 
                | StrOutputParser()
            ).invoke(chain_input)
            
            return {
                "result": result,
                "source_documents": docs,
                "graph_exploration_tool": graph_exploration_tool
            }
        
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            return {
                "result": f"Error processing query: {e}",
                "source_documents": [],
                "graph_exploration_tool": graph_exploration_tool
            }
    
    logger.info("Graph-enhanced RAG chain created successfully")
    return rag_with_sources

class GraphExplorationInput(BaseModel):
    """Input model for graph exploration tool."""
    entity: str = Field(description="The name of the entity to explore in the graph")
    reason: str = Field(description="Brief explanation of why this entity's context is needed", default="Exploring entity context")

class GraphExplorationTool(BaseTool):
    """A tool for exploring graph-based entity context."""
    name: str = "graph_exploration_tool"
    description: str = "Explore detailed context for a specific entity in the campaign's knowledge graph"
    args_schema: Type[BaseModel] = GraphExplorationInput
    
    # Explicitly define graph_builder as a field
    graph_builder: Optional[ObsidianGraphBuilder] = Field(
        default=None, 
        description="Graph builder instance for exploring entity context"
    )
    max_depth: int = Field(
        default=2, 
        description="Maximum depth of context exploration"
    )

    def _run(
        self, 
        entity: str, 
        reason: str = "Exploring entity context for better understanding",
        **kwargs
    ) -> str:
        """
        Run method for graph exploration tool.
        
        :param entity: Name of the entity to explore
        :param reason: Reason for exploring the entity
        :return: Detailed context for the entity
        """
        try:
            # Retrieve the graph builder 
            graph_builder = (
                kwargs.get('graph_builder') or 
                self.graph_builder or 
                ObsidianGraphBuilder(CONTENT_DIR)
            )
            
            # Expand context for the entity
            context = expand_entity_context(entity, graph_builder)
            
            # Log the exploration
            logger.info(f"Exploring entity: {entity}. Reason: {reason}")
            
            return context
        
        except Exception as e:
            error_msg = f"Error exploring entity {entity}: {e}"
            logger.error(error_msg)
            return error_msg

    async def _arun(
        self, 
        entity: str, 
        reason: str = "Exploring entity context for better understanding",
        **kwargs
    ) -> str:
        """
        Async run method for graph exploration tool.
        
        :param entity: Name of the entity to explore
        :param reason: Reason for exploring the entity
        :return: Detailed context for the entity
        """
        return self._run(entity, reason, **kwargs)

def create_graph_exploration_tool(graph_builder: ObsidianGraphBuilder) -> GraphExplorationTool:
    """
    Create a graph exploration tool with a specific graph builder.
    
    :param graph_builder: The ObsidianGraphBuilder instance
    :return: Configured GraphExplorationTool
    """
    # Create the tool with the specific graph builder
    return GraphExplorationTool(graph_builder=graph_builder)

def create_graph_exploration_agent(
    vector_store, 
    graph_path: str, 
    llm_model: str, 
    top_k: int = 4
):
    """
    Create an agent-based RAG system with graph-first exploration
    
    :param vector_store: Existing vector store
    :param graph_path: Path to the exported graph JSON
    :param llm_model: Language model to use
    :param top_k: Number of documents to retrieve
    :return: Agent executor for graph-enhanced RAG
    """
    logger.info("Creating graph-first exploration agent")
    
    # Load graph
    graph = nx.readwrite.json_graph.node_link_graph(
        json.load(open(graph_path, 'r', encoding='utf-8'))
    )
    
    # Initialize graph builder
    graph_builder = ObsidianGraphBuilder(os.path.dirname(graph_path))
    graph_builder.graph = graph
    
    # Create graph exploration tool
    graph_exploration_tool = create_graph_exploration_tool(graph_builder)
    
    # LLM
    llm = ChatOllama(model=llm_model)
    
    def graph_context_retriever(query: str) -> str:
        """
        Retrieve graph-based context for a query
        
        :param query: User query
        :return: Formatted graph context string
        """
        # Extract potential entities from the query
        potential_entities = extract_potential_entities(query, graph)
        
        # If no entities found, return empty string
        if not potential_entities:
            return "No directly related entities found in the graph."
        
        # Prioritize most relevant entities
        top_entities = potential_entities[:3]
        
        # Collect context for top entities
        entity_contexts = []
        for entity in top_entities:
            try:
                # Expand context for each entity
                context = expand_entity_context(entity, graph_builder)
                entity_contexts.append(f"Context for {entity}:\n{context}")
            except Exception as e:
                logger.warning(f"Error expanding context for {entity}: {e}")
        
        return "\n\n".join(entity_contexts)
    
    def vector_context_retriever(query: str) -> str:
        """
        Retrieve vector-based context as a secondary source
        
        :param query: User query
        :return: Formatted vector context string
        """
        try:
            # Perform vector search
            docs = vector_store.similarity_search(query, k=top_k)
            return "\n\n".join([doc.page_content for doc in docs])
        except Exception as e:
            logger.warning(f"Vector search error: {e}")
            return "No vector context available."
    
    # Tools
    tools = [
        Tool(
            name="graph_context",
            func=graph_context_retriever,
            description="Primary context retrieval from the campaign's knowledge graph. Finds and expands context for relevant entities."
        ),
        Tool(
            name="vector_context",
            func=vector_context_retriever,
            description="Secondary context retrieval using vector similarity search. Use only if graph context is insufficient."
        ),
        graph_exploration_tool
    ]
    
    # Prompt template with graph-first reasoning
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an expert D&D campaign assistant with a comprehensive knowledge graph.

Reasoning Strategy (Graph-First Approach):
1. Analyze the query for key entities
2. Retrieve graph-based context for those entities
3. Evaluate the completeness of graph context
4. If graph context is insufficient:
   - Use vector search as a supplementary source
   - Identify gaps in current understanding
   - Use graph exploration tool to fill those gaps
5. Synthesize a comprehensive, accurate response

Available Tools:
- graph_context: Primary context from knowledge graph
- vector_context: Secondary vector-based search
- graph_exploration_tool: Detailed entity exploration

Response Guidelines:
- Prioritize graph-based knowledge
- Be precise and concise
- Explain your reasoning process
- Only use vector search if graph context is truly insufficient
"""),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", """Query: {query}

Graph Context:
{graph_context}

Vector Context (if needed):
{vector_context}"""),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    # Create the agent
    agent = create_tool_calling_agent(llm, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=True,
        max_iterations=3  # Prevent infinite exploration
    )
    
    # Wrapper function to prepare inputs
    def graph_rag_agent(inputs):
        logger.info(f"Processing query: {inputs['query']}")
        
        try:
            # Retrieve graph context
            graph_context = graph_context_retriever(inputs["query"])
            
            # Retrieve vector context (as backup)
            vector_context = vector_context_retriever(inputs["query"])
            
            # Run agent
            result = agent_executor.invoke({
                "query": inputs["query"],
                "graph_context": graph_context,
                "vector_context": vector_context
            })
            
            return {
                "result": result['output'],
                "graph_context": graph_context,
                "vector_context": vector_context,
                "graph_exploration_tool": graph_exploration_tool
            }
        
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            return {
                "result": f"Error processing query: {e}",
                "graph_context": "",
                "vector_context": "",
                "graph_exploration_tool": graph_exploration_tool
            }
    
    logger.info("Graph-first exploration agent created successfully")
    return graph_rag_agent


