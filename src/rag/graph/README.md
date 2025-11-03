# Knowledge Graph Tools and Agents

## Overview

This module provides a set of LangChain-compatible tools and agents for navigating and exploring the campaign knowledge graph.

## Components

### Tools (`tools.py`)

The `tools.py` module defines three main tools:

1. `SearchEntityTool`: Search for entities in the knowledge graph by name or alias
2. `EntityDetailsTool`: Retrieve comprehensive details for a specific entity
3. `RelatedEntitiesTool`: Find related entities with a specified maximum depth

### Agents (`agents.py`)

The `agents.py` module provides:

- `create_graph_agent()`: A flexible function to create graph-based agents with configurable tools
- Specific agent creators:
  - `search_agent()`: Agent focused on entity search
  - `entity_details_agent()`: Agent for retrieving entity details
  - `related_entities_agent()`: Agent for finding related entities

## Usage Example

```python
from src.rag.graph.agents import create_graph_exploration_chain

# Create a chain of graph exploration agents
chain = create_graph_exploration_chain()

# Use the chain sequentially
search_result = chain[0].invoke({"input": "Find characters related to magic"})
details_result = chain[1].invoke({"input": "Get details about the most interesting character"})
related_result = chain[2].invoke({"input": "Find entities related to the previous character"})
```

## Configuration

- Customize agents by specifying different tools, models, or temperatures
- Use `get_graph_tools()` to access all available graph tools
- Modify the system prompt in `create_graph_agent()` to adjust agent behavior

## Dependencies

- LangChain
- OpenAI
- NetworkX
- Pydantic
