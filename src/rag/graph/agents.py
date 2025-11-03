from typing import List, Optional, Dict, Any

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import BaseTool
from langchain.memory import ConversationBufferMemory

from src.agents.tools import (
    SearchEntityTool, 
    EntityDetailsTool, 
    RelatedEntitiesTool, 
    get_graph_tools
)

def create_graph_agent(
    tools: Optional[List[BaseTool]] = None, 
    model_name: str = "gpt-3.5-turbo",
    temperature: float = 0.3
) -> AgentExecutor:
    """
    Create a graph-based agent with specified tools and configuration.
    
    :param tools: List of tools to use (defaults to all graph tools)
    :param model_name: OpenAI model to use
    :param temperature: Sampling temperature for the model
    :return: Configured AgentExecutor
    """
    # Use default graph tools if none provided
    if tools is None:
        tools = get_graph_tools()
    
    # Initialize the language model
    llm = ChatOpenAI(
        model=model_name, 
        temperature=temperature
    )
    
    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert knowledge graph navigator. "
         "Use the available tools to explore and retrieve information "
         "from the campaign knowledge base."),
        MessagesPlaceholder(variable_name="chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])
    
    # Create memory for conversation history
    memory = ConversationBufferMemory(
        memory_key="chat_history", 
        return_messages=True
    )
    
    # Create the agent
    agent = create_openai_tools_agent(
        llm=llm, 
        tools=tools, 
        prompt=prompt
    )
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent_executor

# Convenience functions for specific agent types
def search_agent() -> AgentExecutor:
    """Create an agent focused on entity search."""
    return create_graph_agent(
        tools=[SearchEntityTool()], 
        temperature=0.2
    )

def entity_details_agent() -> AgentExecutor:
    """Create an agent focused on retrieving entity details."""
    return create_graph_agent(
        tools=[EntityDetailsTool()], 
        temperature=0.1
    )

def related_entities_agent() -> AgentExecutor:
    """Create an agent focused on finding related entities."""
    return create_graph_agent(
        tools=[RelatedEntitiesTool()], 
        temperature=0.2
    )

# Convenience function to create a chain of agents
def create_graph_exploration_chain(
    steps: Optional[List[AgentExecutor]] = None
) -> List[AgentExecutor]:
    """
    Create a chain of graph exploration agents.
    
    :param steps: Optional list of agents to use in the chain
    :return: List of agents that can be chained together
    """
    if steps is None:
        steps = [
            search_agent(),
            entity_details_agent(),
            related_entities_agent()
        ]
    
    return steps
