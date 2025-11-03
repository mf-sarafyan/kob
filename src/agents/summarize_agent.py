import logging
from typing import Dict, List, Any, Optional

from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

from src.settings import CONTENT_DIR, INDEX_DIR
from src.rag import create_knowledge_graph

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Prompt template for content summarization
content_summarizer_prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are an expert knowledge base summarizer for a D&D campaign. "
     "Your task is to generate a comprehensive, precise response to the query "
     "using ONLY the provided document contents.\n\n"
     "Guidelines:\n"
     "1. Focus EXCLUSIVELY on the content provided\n"
     "2. Synthesize information directly from the given text\n"
     "3. Provide a clear, concise, and informative response\n"
     "4. Do NOT rely on any external knowledge or previous context\n"
     "5. If the content is insufficient to answer the query, state that clearly\n\n"
     "Output Requirements:\n"
     "- Directly answer the original query\n"
     "- Use ONLY information from the provided document contents\n"
     "- Be objective and comprehensive within the limits of the given text\n"
     "- If no clear answer can be found, explain why\n"
     "- Output plain text only, no JSON or special formatting"
    ),
    ("user", 
     "Query: {query}\n\n"
     "Available Document Contents:\n{available_documents}\n\n"
     "Generate a response using ONLY the information in these documents."
    )
])

# LLM for content summarization
content_summarizer_llm = ChatOllama(
    model="qwen2.5:7b-instruct",  # or "llama3.1:8b-instruct"
    temperature=0.3,
    num_ctx=2048,
)

# String output parser for content summarization
content_summarizer_parser = StrOutputParser()

# Combine prompt, LLM, and parser
content_summarizer_chain = content_summarizer_prompt | content_summarizer_llm | content_summarizer_parser

class SummarizeAgent:
    def __init__(
        self, 
        content_dir: str = CONTENT_DIR,
        index_dir: str = INDEX_DIR
    ):
        """
        Initialize the summarize agent
        
        :param content_dir: Directory containing content
        :param index_dir: Directory for storing indexes
        """
        # Create Knowledge Graph
        self.knowledge_graph = create_knowledge_graph(
            content_dir=content_dir, 
            index_dir=index_dir
        )
    
    def retrieve_document_contents(self, selected_documents: List[str]) -> Dict[str, str]:
        """
        Retrieve full contents for selected documents
        
        :param selected_documents: List of document names to retrieve
        :return: Dictionary of document contents
        """
        try:
            # Use knowledge graph to retrieve document contents
            return {
                doc: self.knowledge_graph.get_entity_details(doc).get('content', {}).get('full_content', 'No content available')
                for doc in selected_documents
            }
        except Exception as e:
            logger.error(f"Error retrieving document contents: {e}")
            return {
                doc: f"Error retrieving content: {str(e)}" 
                for doc in selected_documents
            }
    
    def summarize_context(self, query: str, selected_documents: List[str]) -> Dict[str, Any]:
        """
        Summarize context for the given query using selected documents
        
        :param query: Original user query
        :param selected_documents: List of documents to use for summarization
        :return: Summarized response
        """
        try:
            # Retrieve document contents
            document_contents = self.retrieve_document_contents(selected_documents)
            
            # Prepare input for summarization
            prompt_input = {
                'query': query,
                'available_documents': "\n\n---\n\n".join([
                    f"Document: {name}\nContent:\n{content}" 
                    for name, content in document_contents.items() 
                    if content and content.strip() != f"Error retrieving content: {name}"
                ])
            }
            
            # If no meaningful documents, return early
            if not prompt_input['available_documents']:
                return {
                    'selected_documents': selected_documents,
                    'document_contents': document_contents,
                    'summary': "No meaningful content was found in the provided documents.",
                    'error': "No usable document contents"
                }
            
            # Invoke content summarizer - now returns plain text
            summary_text = content_summarizer_chain.invoke(prompt_input)
            
            # Combine results
            return {
                'selected_documents': selected_documents,
                'document_contents': document_contents,
                'summary': summary_text
            }
        
        except Exception as e:
            logger.error(f"Summarization error: {e}")
            return {
                'selected_documents': selected_documents,
                'document_contents': {},
                'summary': None,
                'error': str(e)
            }
    
    def __call__(self, query: str, document_contents: Any) -> Dict[str, Any]:
        """
        Summarize context using document contents
        
        :param query: Original user query
        :param document_contents: Document contents to summarize (expected: Dict[str, str])
        :return: Summarized context
        """
        # Comprehensive debugging
        logger.info("=== Summarization Input Debug ===")
        logger.info(f"Query: {query}")
        logger.info(f"Document Contents Type: {type(document_contents)}")
        
        # Attempt to convert input to dictionary if it's not already
        try:
            if isinstance(document_contents, list):
                logger.warning("Input is a list, attempting to convert to dictionary")
                # If it's a list of dictionaries, try to extract contents
                if all(isinstance(item, dict) for item in document_contents):
                    # Attempt to extract 'name' and 'content' from each dict
                    document_contents = {
                        item.get('name', f'Document_{i}'): item.get('content', '') 
                        for i, item in enumerate(document_contents)
                    }
                else:
                    # If simple list, convert to dict with index as key
                    document_contents = {
                        f'Document_{i}': str(item) 
                        for i, item in enumerate(document_contents)
                    }
            
            # Ensure we have a dictionary
            if not isinstance(document_contents, dict):
                raise TypeError(f"Cannot convert input of type {type(document_contents)} to dictionary")
            
            # Log the converted contents
            logger.info("Converted Document Contents:")
            for name, content in document_contents.items():
                logger.info(f"  {name}: {content[:100]}...")  # Log first 100 chars
        
        except Exception as conversion_error:
            logger.error(f"Error converting document contents: {conversion_error}")
            return {
                'selected_documents': [],
                'document_contents': {},
                'summary': f"Error processing document contents: {conversion_error}",
                'error': str(conversion_error)
            }
        
        # Validate input
        if not document_contents:
            return {
                'selected_documents': [],
                'document_contents': {},
                'summary': "No documents were provided for summarization.",
                'error': "Empty document contents"
            }
        
        # Prepare input for summarization
        prompt_input = {
            'query': query,
            'available_documents': "\n\n---\n\n".join([
                f"Document: {name}\nContent:\n{content}" 
                for name, content in document_contents.items() 
                if content and content.strip() != f"No content available for {name}"
            ])
        }
        
        # Check if there are any meaningful documents
        if not prompt_input['available_documents']:
            return {
                'selected_documents': list(document_contents.keys()),
                'document_contents': document_contents,
                'summary': "No meaningful content was found in the provided documents.",
                'error': "No usable document contents"
            }
        
        # Invoke content summarizer - now returns plain text
        summary_text = content_summarizer_chain.invoke(prompt_input)
        
        # Combine results
        return {
            'selected_documents': list(document_contents.keys()),
            'document_contents': document_contents,
            'summary': summary_text
        }

def create_summarize_agent(
    content_dir: str = CONTENT_DIR, 
    index_dir: str = INDEX_DIR
) -> SummarizeAgent:
    """
    Create a summarize agent
    
    :param content_dir: Directory containing content
    :param index_dir: Directory for storing indexes
    :return: Configured SummarizeAgent
    """
    return SummarizeAgent(
        content_dir=content_dir, 
        index_dir=index_dir
    )

# Main execution for testing
if __name__ == '__main__':
    from src.agents.search_agent import create_search_agent
    from src.agents.expand_agent import create_expand_agent
    
    # Create agents
    search_agent = create_search_agent()
    expand_agent = create_expand_agent()
    summarize_agent = create_summarize_agent()
    
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
    
    # Run full pipeline
    import json
    for query in test_queries:
        print(f"\n=== Query: {query} ===")
        
        # Perform search
        search_result = search_agent(query)
        
        # Expand context
        expand_result = expand_agent(query, search_result)
        
        # Select documents
        document_contents = expand_result['document_contents']
        
        # Summarize
        summary_result = summarize_agent(query, document_contents)
        
        print(json.dumps(summary_result, indent=2))
