import logging
from typing import Dict, Any

from src.settings import CONTENT_DIR, INDEX_DIR
from src.agents.search_agent import create_search_agent
from src.agents.expand_agent import create_expand_agent
from src.agents.summarize_agent import create_summarize_agent

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ContextAugmenterAgent:
    def __init__(
        self, 
        content_dir: str = CONTENT_DIR,
        index_dir: str = INDEX_DIR,
        model: str = "qwen2.5:7b-instruct"
    ):
        """
        Initialize the context augmenter agent with modular components
        
        :param content_dir: Directory containing content
        :param index_dir: Directory for storing indexes
        :param model: Specific model to use for search planning
        """
        # Create modular agents
        self.search_agent = create_search_agent(
            content_dir=content_dir, 
            index_dir=index_dir,
            model=model
        )
        
        self.expand_agent = create_expand_agent(
            content_dir=content_dir, 
            index_dir=index_dir
        )
        
        self.summarize_agent = create_summarize_agent(
            content_dir=content_dir, 
            index_dir=index_dir
        )
    
    def __call__(self, query: str) -> Dict[str, Any]:
        """
        Full context augmentation pipeline
        
        :param query: User query to augment
        :return: Comprehensive context and response
        """
        # Perform search
        search_result = self.search_agent(query)
        
        # Expand context
        expand_result = self.expand_agent(query, search_result)
        
        # Select documents
        document_contents = expand_result['document_contents']
        
        # Summarize context
        summary_result = self.summarize_agent(query, document_contents)
        
        # Combine all results
        final_result = {
            'query': query,
            **search_result,
            **expand_result,
            **summary_result
        }
        
        return final_result

def create_context_augmenter(
    content_dir: str = CONTENT_DIR, 
    index_dir: str = INDEX_DIR,
    model: str = "qwen2.5:7b-instruct"
) -> ContextAugmenterAgent:
    """
    Create a context augmentation agent
    
    :param content_dir: Directory containing content
    :param index_dir: Directory for storing indexes
    :param model: Specific model to use for search planning
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
        "What's the Rock of Bral political structure",
        "Who is Baang",
        "Who are the Keepers?",
        "Who is Vax",
        "What are the current events in the campaign",
        "How do I set up a Bastion?", 
        "What is The Spelljammer",
        "Quem é Keeper of Whispers?"
    ]
    
    # Add debug flag (default to False)
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description='Context Augmenter Debug Tool')
    parser.add_argument('--debug', action='store_true', 
                        help='Print full JSON output')
    args = parser.parse_args()
    
    # Run augmentation for each query
    for query in test_queries:
        print(f"\n=== Query: {query} ===")
        result = context_augmenter(query)
        
        # Print summary
        if result.get('summary'):
            print("\nSummary:")
            print(result['summary'])
        
        # If debug flag is set, print full JSON
        if args.debug:
            print("\nFull Result:")
            print(json.dumps(result, indent=2))