import os
import sys
from pathlib import Path
import streamlit as st
from typing import Dict, Any, List

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.settings import CONTENT_DIR, INDEX_DIR
from src.agents.tool_augmenter import create_tool_augmenter
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

# Page configuration
st.set_page_config(
    page_title="Keepers' Compendium Chat",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "tool_augmenter" not in st.session_state:
    st.session_state.tool_augmenter = None
if "initialized" not in st.session_state:
    st.session_state.initialized = False

@st.cache_resource
def initialize_agent():
    """Initialize the tool augmenter agent (cached)"""
    try:
        return create_tool_augmenter(
            content_dir=CONTENT_DIR,
            index_dir=INDEX_DIR
        )
    except Exception as e:
        st.error(f"Failed to initialize agent: {e}")
        return None

def main():
    """Main Streamlit application"""
    
    # Sidebar configuration
    with st.sidebar:
        st.title("⚔️ Keepers' Compendium")
        st.markdown("### Chat with your D&D Campaign Knowledge Base")
        
        st.markdown("---")
        
        # Initialize button
        if not st.session_state.initialized:
            if st.button("🚀 Initialize Agent", type="primary", use_container_width=True):
                with st.spinner("Initializing agent..."):
                    st.session_state.tool_augmenter = initialize_agent()
                    if st.session_state.tool_augmenter:
                        st.session_state.initialized = True
                        st.success("Agent initialized!")
                        st.rerun()
        else:
            st.success("✅ Agent Ready")
            if st.button("🔄 Reinitialize", use_container_width=True):
                st.session_state.initialized = False
                st.session_state.tool_augmenter = None
                st.session_state.messages = []
                st.cache_resource.clear()
                st.rerun()
        
        st.markdown("---")
        
        # Model info
        st.markdown("### Model Info")
        st.info("Using OpenRouter API with GPT-4o")
        
        st.markdown("---")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
    
    # Main content area
    st.title("⚔️ Keepers' Compendium Chat")
    st.markdown("Ask questions about your D&D campaign - characters, locations, factions, rules, and more!")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Show tool calls if available
            if message["role"] == "assistant" and "tool_calls" in message:
                tool_calls = message["tool_calls"]
                if tool_calls:
                    with st.expander(f"🔧 Tool Calls ({len(tool_calls)})"):
                        for i, call in enumerate(tool_calls, 1):
                            st.markdown(f"**{i}. {call.get('tool', 'unknown')}**")
                            if call.get('tool_input'):
                                st.json(call['tool_input'])
    
    # Helper function to convert Streamlit messages to LangChain messages
    def convert_messages_to_langchain(messages: List[Dict[str, Any]]) -> List[BaseMessage]:
        """Convert Streamlit message format to LangChain message format"""
        langchain_messages = []
        for msg in messages:
            if msg["role"] == "user":
                langchain_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                langchain_messages.append(AIMessage(content=msg["content"]))
        return langchain_messages
    
    # Chat input
    if st.session_state.initialized and st.session_state.tool_augmenter:
        if prompt := st.chat_input("Ask a question about your campaign..."):
            # Add user message
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Display user message
            with st.chat_message("user"):
                st.markdown(prompt)
            
            # Generate response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        # Convert previous messages to LangChain format (exclude the current one)
                        previous_messages = st.session_state.messages[:-1]  # All but the current prompt
                        chat_history = convert_messages_to_langchain(previous_messages) if previous_messages else None
                        
                        # Call agent with chat history
                        result = st.session_state.tool_augmenter(prompt, chat_history=chat_history)
                        
                        # Display answer
                        answer = result.get("answer", "No answer generated.")
                        st.markdown(answer)
                        
                        # Add assistant message with tool calls
                        assistant_message = {
                            "role": "assistant",
                            "content": answer,
                            "tool_calls": result.get("tool_calls", [])
                        }
                        st.session_state.messages.append(assistant_message)
                        
                        # Show tool calls in expander
                        tool_calls = result.get("tool_calls", [])
                        if tool_calls:
                            with st.expander(f"🔧 Tool Calls ({len(tool_calls)})"):
                                for i, call in enumerate(tool_calls, 1):
                                    st.markdown(f"**{i}. {call.get('tool', 'unknown')}**")
                                    if call.get('tool_input'):
                                        st.json(call['tool_input'])
                                    if call.get('result'):
                                        st.text_area(
                                            f"Result {i}",
                                            call['result'],
                                            height=100,
                                            disabled=True,
                                            key=f"result_{i}"
                                        )
                        
                        # Show success/error status
                        if result.get("success"):
                            st.success("Query completed successfully")
                        else:
                            st.error(f"Error: {result.get('error', 'Unknown error')}")
                    
                    except Exception as e:
                        error_msg = f"An error occurred: {str(e)}"
                        st.error(error_msg)
                        st.session_state.messages.append({
                            "role": "assistant",
                            "content": error_msg
                        })
    else:
        # Not initialized - show instruction
        st.info("👈 Click 'Initialize Agent' in the sidebar to get started!")
        
        # Example queries
        st.markdown("### Example Queries")
        example_queries = [
            "What's the Rock of Bral political structure?",
            "Who is Baang?",
            "Who are the Keepers?",
            "Who is Vax?",
            "What are the current events in the campaign?",
            "How do I set up a Bastion?",
            "What is The Spelljammer?"
        ]
        
        for query in example_queries:
            if st.button(query, key=f"example_{query}", use_container_width=True):
                st.session_state.example_query = query
                if st.session_state.initialized:
                    st.rerun()

# Call main function - Streamlit runs this script top to bottom
main()

