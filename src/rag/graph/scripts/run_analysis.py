#!/usr/bin/env python3
"""
Script to run comprehensive graph analysis for the campaign knowledge base.
"""

import os
import sys
import logging
import argparse
import json

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, project_root)

from src.settings import INDEX_DIR
from src.rag import create_knowledge_graph
from src.rag.graph.graph_builder import create_graph_rag_index

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def interactive_graph_explorer(kg):
    """
    Interactive graph exploration function
    
    :param kg: KnowledgeGraph instance
    """
    while True:
        print("\n--- Graph Explorer ---")
        print("1. Find Entity")
        print("2. Get Entity Details")
        print("3. Get Related Entities")
        print("4. Graph Overview")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        try:
            if choice == '1':
                # Find Entity
                search_term = input("Enter search term: ").strip()
                entities = kg.find_entity(search_term)
                if entities:
                    print("\nMatching Entities:")
                    for entity in entities:
                        print(f"- {entity['node']} (Type: {entity['type']})")
                else:
                    print("No entities found.")
            
            elif choice == '2':
                # Get Entity Details
                entity_name = input("Enter entity name: ").strip()
                try:
                    details = kg.get_entity_details(entity_name)
                    print("\nEntity Details:")
                    print(json.dumps(details, indent=2))
                except Exception as e:
                    print(f"Error retrieving entity details: {e}")
            
            elif choice == '3':
                # Get Related Entities
                entity_name = input("Enter entity name: ").strip()
                try:
                    related = kg.get_related_entities(entity_name)
                    print("\nRelated Entities:")
                    print(json.dumps(related, indent=2))
                except Exception as e:
                    print(f"Error retrieving related entities: {e}")
            
            elif choice == '4':
                # Graph Overview
                connectivity_report = kg.analyze_graph_connectivity()
                print("\nGraph Overview:")
                print(json.dumps(connectivity_report, indent=2))
            
            elif choice == '5':
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    """
    Run comprehensive graph analysis
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Run comprehensive graph analysis')
    parser.add_argument('--visualize', action='store_true', 
                        help='Generate graph visualization')
    parser.add_argument('--output', type=str, default=INDEX_DIR, 
                        help='Output directory for analysis results (default: .rag_index)')
    parser.add_argument('--entity', type=str, 
                        help='Analyze a specific entity in depth')
    parser.add_argument('--interactive', action='store_true',
                        help='Start interactive graph explorer')
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Create knowledge graph
        kg = create_knowledge_graph()
        
        # Ensure output directory exists
        os.makedirs(args.output, exist_ok=True)
        
        # Analyze graph connectivity
        connectivity_report = kg.analyze_graph_connectivity()
        
        logger.info("Graph Connectivity Report:")
        for key, value in connectivity_report.items():
            logger.info(f"{key}: {value}")
        
        # Save connectivity report
        with open(os.path.join(args.output, 'connectivity_report.json'), 'w') as f:
            json.dump(connectivity_report, f, indent=2)
        
        # Optional: Visualize graph
        if args.visualize:
            visualization_path = os.path.join(args.output, 'graph_visualization.png')
            kg.visualize_graph(visualization_path)
            logger.info(f"Graph visualization saved to {visualization_path}")
        
        # Optional: Analyze specific entity
        if args.entity:
            entity_details = kg.get_entity_details(args.entity)
            related_entities = kg.get_related_entities(args.entity)
            
            # Save entity analysis
            with open(os.path.join(args.output, f'{args.entity}_details.json'), 'w') as f:
                json.dump({
                    'entity_details': entity_details,
                    'related_entities': related_entities
                }, f, indent=2)
            
            logger.info(f"Detailed analysis for entity '{args.entity}' saved")
        
        # Optional: Start interactive explorer
        if args.interactive:
            interactive_graph_explorer(kg)
        
        logger.info("Graph analysis completed successfully.")
    
    except Exception as e:
        logger.error(f"Error during graph analysis: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
