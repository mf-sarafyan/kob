#!/usr/bin/env python3
"""
Script to regenerate the graph index for the campaign knowledge base.
"""

import os
import sys
import logging

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.rag import create_knowledge_graph

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """
    Regenerate the graph index
    """
    try:
        # Create knowledge graph (this will automatically build/save the graph)
        kg = create_knowledge_graph()
        
        # Analyze graph connectivity
        connectivity_report = kg.analyze_graph_connectivity()
        
        logger.info("Graph Connectivity Report:")
        for key, value in connectivity_report.items():
            logger.info(f"{key}: {value}")
        
        # Optional: Visualize graph
        kg.visualize_graph('graph_visualization.png')
        
        logger.info("Graph index regeneration completed successfully.")
    
    except Exception as e:
        logger.error(f"Error regenerating graph index: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
