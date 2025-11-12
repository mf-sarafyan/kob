"""
Test configuration with test queries and expected outcomes.

Each test case defines:
- query: The test query to run
- expected_entities: List of entity names that should be found/mentioned
- expected_facts: List of specific facts that should be present in the answer
- description: Human-readable description of what this test validates
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class TestCase:
    """A single test case definition."""
    query: str
    expected_entities: Optional[List[str]] = None
    expected_facts: Optional[List[str]] = None
    description: Optional[str] = None
    skip: bool = False
    
    def __post_init__(self):
        """Set defaults."""
        if self.expected_entities is None:
            self.expected_entities = []
        if self.expected_facts is None:
            self.expected_facts = []
        if self.description is None:
            self.description = self.query


# Test queries moved from tool_augmenter.py
TEST_CASES = [
    TestCase(
        query="What's the Rock of Bral political structure",
        expected_entities=["Rock of Bral"],
        expected_facts=[],
        description="Should find information about Rock of Bral's political structure"
    ),
    TestCase(
        query="Who is Baang",
        expected_entities=["Baang"],
        expected_facts=[],
        description="Should find entity Baang"
    ),
    TestCase(
        query="Who are the Keepers fighting against?",
        expected_entities=["Keepers"],
        expected_facts=[],
        description="Should find information about Keepers' enemies/opponents"
    ),
    TestCase(
        query="Who is Vax",
        expected_entities=["Vax"],
        expected_facts=[],
        description="Should find entity Vax"
    ),
    TestCase(
        query="What are the current events in the campaign",
        expected_entities=[],
        expected_facts=[],
        description="Should retrieve current campaign events"
    ),
    TestCase(
        query="How do I set up a Bastion?",
        expected_entities=["Bastion"],
        expected_facts=[],
        description="Should find information about setting up a Bastion"
    ),
    TestCase(
        query="What is The Spelljammer",
        expected_entities=["Spelljammer"],
        expected_facts=[],
        description="Should find information about The Spelljammer"
    ),
    TestCase(
        query="Em que mundo (planeta e Wildspace System) fica o Black Dragon Inn?",
        expected_entities=["Black Dragon Inn"],
        expected_facts=[],
        description="Should find the world/planet and Wildspace System where Black Dragon Inn is located"
    ),
    TestCase(
        query="Onde é o bar do Large Luigi?",
        expected_entities=["Large Luigi"],
        expected_facts=[],
        description="Should find the location of Large Luigi's bar"
    ),
    TestCase(
        query="Onde eu posso encontrar o Mordenkainen?",
        expected_entities=["Mordenkainen"],
        expected_facts=[],
        description="Should find where Mordenkainen can be found"
    ),
]

