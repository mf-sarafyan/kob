import os
import logging
from typing import Dict, List, Any, Optional
from enum import Enum

from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import ChatOllama

from src.settings import CONTENT_DIR, INDEX_DIR
from src.rag import create_knowledge_graph, create_rag_index
from src.agents.tools import create_search_tools

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Enum for entity types based on wiki structure
class EntityType(str, Enum):
    CHARACTER = "character"
    FACTION = "faction"
    LOCATION = "location"
    ITEM = "item"
    ENTRY = "entry"

# Pydantic model for search planning
class SearchPlan(BaseModel):
    vector_queries: List[str] = Field(default_factory=list)
    graph_entities: List[str] = Field(default_factory=list)
    filters: Optional[Dict[str, Any]] = Field(default_factory=dict)
    error: Optional[str] = None

# Ontology description
ontology = (
  "Vault ontology:\n"
  "- type ∈ {{character, location, faction, item, entry}}\n"
  "- filters supports ONLY one field: entity_type (same set as type).\n"
  "- Use graph_entities for proper nouns (NPCs, facções, locais, itens).\n"
  "- Use vector_queries for natural language searches.\n"
  "- If no clear entity_type applies, omit filters."
)

# Prompt template
search_planner_prompt = ChatPromptTemplate.from_messages([
  ("system",
   "You are a search planner for a D&D campaign knowledge base. "
   "Return ONLY valid JSON matching this schema:\n"
   "- vector_queries: List[str] for semantic searches\n"
   "- graph_entities: List[str] for specific entities\n"
   "- filters: Optional entity type filter\n"
   "\n" + ontology),
  # One EN example
  ("user", "Who runs Montevia and who are their allies?"),
  ("assistant",
   '{{"vector_queries":["Who runs Montevia","Montevia allies"],'
   '"graph_entities":["Montevia"],'
   '"filters":{{"entity_type":"faction"}}}}'),
  # One PT example
  ("user", "Onde fica o Red Spiral e quem controla a área?"),
  ("assistant",
   '{{"vector_queries":["Onde fica Red Spiral","quem controla Red Spiral"],'
   '"graph_entities":["Red Spiral"],'
   '"filters":{{"entity_type":"location"}}}}'),
  # Actual user input
  ("human", "{query}")
])

# LLM for search planning
search_planner_llm = ChatOllama(
    model="qwen2.5:7b-instruct",  # or "llama3.1:8b-instruct"
    temperature=0.0,
    num_ctx=1024,
)

# JSON output parser
search_planner_parser = JsonOutputParser(pydantic_object=SearchPlan)

# Combine prompt, LLM, and parser
search_planner_chain = search_planner_prompt | search_planner_llm | search_planner_parser

class SearchAgent:
    def __init__(
        self, 
        content_dir: str = CONTENT_DIR,
        index_dir: str = INDEX_DIR,
        model: str = "qwen2.5:7b-instruct"
    ):
        """
        Initialize the search agent
        
        :param content_dir: Directory containing content
        :param index_dir: Directory for storing indexes
        :param model: Specific model to use for search planning
        """
        # Create Knowledge Graph (for graph-only operations)
        self.knowledge_graph = create_knowledge_graph(
            content_dir=content_dir, 
            index_dir=index_dir
        )
        
        # Create RAG index to get vector store and graph builder
        vector_store, graph_builder, _ = create_rag_index(
            content_dir=content_dir,
            index_dir=index_dir
        )
        
        # Create search tools
        self.vector_search_tool, self.graph_search_tool = create_search_tools(
            vector_store, 
            graph_builder
        )
        
        # Prepare search planner
        self.search_planner = search_planner_chain
    
    def plan_search(self, query: str) -> Dict[str, Any]:
        """
        Plan search strategy for a given query
        
        :param query: User query to plan search for
        :return: Structured search plan
        """
        try:
            # Generate search plan
            search_plan = self.search_planner.invoke({"query": query})
            
            return {
                'query': query,
                'search_plan': search_plan,
                'error': search_plan.get("error", None)
            }
        
        except Exception as e:
            logger.error(f"Search planning error: {e}")
            return {
                'query': query,
                'search_plan': {},
                'error': str(e)
            }
    
    def execute_search(self, search_plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute search based on the search plan
        
        :param search_plan: Structured search plan
        :return: Search results
        """
        try:
            # Execute vector searches
            vector_results = []
            for vector_query in search_plan.get("search_plan", {}).get("vector_queries", []):
                try:
                    vector_result = self.vector_search_tool._run(vector_query)
                    vector_results.append({
                        'query': vector_query,
                        'results': vector_result
                    })
                except Exception as vec_err:
                    logger.error(f"Vector search error for query '{vector_query}': {vec_err}")
            
            # Execute graph searches
            graph_results = []
            for entity in search_plan.get("search_plan", {}).get("graph_entities", []):
                try:
                    # Use the new knowledge graph search method
                    graph_result = self.knowledge_graph.find_entity(entity)
                    graph_results.append({
                        'entity': entity,
                        'results': graph_result
                    })
                except Exception as graph_err:
                    logger.error(f"Graph search error for entity '{entity}': {graph_err}")
            
            # Prepare final result
            return {
                **search_plan,
                'vector_searches': vector_results,
                'graph_searches': graph_results,
                'filters': search_plan.get("search_plan", {}).get("filters", {})
            }
        
        except Exception as e:
            logger.error(f"Search execution error: {e}")
            return {
                **search_plan,
                'vector_searches': [],
                'graph_searches': [],
                'filters': {},
                'error': str(e)
            }
    
    def __call__(self, query: str) -> Dict[str, Any]:
        """
        Full search process
        
        :param query: User query to search
        :return: Comprehensive search results
        """
        # Plan the search
        search_plan = self.plan_search(query)
        
        # Execute the search
        search_results = self.execute_search(search_plan)
        
        return search_results

def create_search_agent(
    content_dir: str = CONTENT_DIR, 
    index_dir: str = INDEX_DIR,
    model: str = "qwen2.5:7b-instruct"
) -> SearchAgent:
    """
    Create a search agent
    
    :param content_dir: Directory containing content
    :param index_dir: Directory for storing indexes
    :param model: Specific model to use for search planning
    :return: Configured SearchAgent
    """
    return SearchAgent(
        content_dir=content_dir, 
        index_dir=index_dir,
        model=model
    )

# Main execution for testing
if __name__ == '__main__':
    # Create search agent
    search_agent = create_search_agent()
    
    # Test queries
    test_queries = [
        "What's the Rock of Bral political structure",
        "Who is Baang",
        "Who are the Keepers?",
        "Who is Vax",
        "What are the current events in the campaign",
        "How do I set up a Bastion?", 
        "What is The Spelljammer"
    ]
    
    # Run searches
    import json
    for query in test_queries:
        print(f"\n=== Query: {query} ===")
        result = search_agent(query)
        print(json.dumps(result, indent=2))
