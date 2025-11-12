"""
Deprecated agents - kept for reference.

These agents were replaced by the tool_augmenter.py which uses a single
tool-calling agent instead of the three-step process (search -> expand -> summarize).
"""

from .context_augmenter import (
    ContextAugmenterAgent,
    create_context_augmenter
)
from .search_agent import (
    SearchAgent,
    create_search_agent
)
from .expand_agent import (
    ExpandAgent,
    create_expand_agent
)
from .summarize_agent import (
    SummarizeAgent,
    create_summarize_agent
)

__all__ = [
    'ContextAugmenterAgent',
    'create_context_augmenter',
    'SearchAgent',
    'create_search_agent',
    'ExpandAgent',
    'create_expand_agent',
    'SummarizeAgent',
    'create_summarize_agent'
]

