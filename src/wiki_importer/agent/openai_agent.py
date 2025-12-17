from __future__ import annotations
import json
import os
from typing import Any
from src.wiki_importer.agent.types import AgentInput, AgentOutput
from src.wiki_importer.agent.prompts import build_prompt
from src.wiki_importer.configs.settings import NoteType

# Try to import secrets, fallback to environment variable
try:
    from src.secrets import OPENROUTER_API_KEY
except ImportError:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")


def run_agent(inp: AgentInput) -> AgentOutput:
    """
    Produces:
      - frontmatter dict (minus image; composer can inject)
      - markdown body content
    """
    # Keep the LLM dependency optional: import inside.
    from openai import OpenAI  # type: ignore

    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

    prompt = build_prompt(inp.entry_type, inp.title, inp.raw_text)

    resp = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    body = resp.choices[0].message.content.strip()

    fm = {
        "title": inp.title,
        "source": inp.source,
        "source_url": inp.source_url,
        "tags": ["wiki-import"],
        "author": "agent",
    }

    return AgentOutput(entry_type=inp.entry_type, frontmatter=fm, content=body)


def build_json_extraction_prompt(note_type: NoteType, title: str, raw_text: str, available_params: list[str]) -> str:
    """Build a prompt that asks the agent to extract structured JSON data."""
    params_list = ", ".join(available_params) if available_params else "none"
    
    return f"""
You are extracting structured information from a wiki article for a D&D campaign note.

Note type: {note_type}
Title: {title}

Available parameters for this note type: {params_list}

Extract information from the article and return ONLY a valid JSON object with the following structure:
{{
  "title": "{title}",
  "type": "{note_type}",
  "parameters": {{
    // Fill in values for the available parameters based on the article content
    // Use null for parameters that cannot be determined from the article
    // For list parameters (like known_locations, factions, appears_in), use arrays
    // Example: "known_locations": ["Location 1", "Location 2"]
  }},
  "summary": "A markdown-formatted summary covering each major section of the article. Use ## headers for each section (Description, Behavior, Ecology, History, etc.) and provide 2-4 sentences per section summarizing key points. Example format:\n\n## Description\n\nBrief description of appearance and nature.\n\n## Behavior\n\nHow it acts and interacts.\n\n## Ecology\n\nHabitat and role in the world."
}}

Rules:
- Do NOT invent information that isn't in the article
- Use null for parameters that cannot be determined
- Extract only game-relevant information
- Return ONLY valid JSON, no markdown formatting outside the summary field
- The summary field should contain markdown-formatted text with section headers
- For array fields (known_locations, factions, appears_in), always use arrays even if empty
- Summarize each major section of the article (Description, Behavior, Ecology, History, etc.) rather than reducing everything to 2-3 sentences

Article text (truncated if too long):

{raw_text[:8000]}

""".strip()


def extract_json_structured_data(
    note_type: NoteType,
    title: str,
    raw_text: str,
    available_params: list[str],
) -> dict[str, Any]:
    """
    Extract structured JSON data from wiki article text using LLM.
    
    Args:
        note_type: Type of note (creature, faction, location, character, item, entry)
        title: Article title
        raw_text: Raw article text content
        available_params: List of available parameters for this note type
    
    Returns:
        Dictionary containing extracted structured data
    
    Raises:
        json.JSONDecodeError: If LLM response is not valid JSON
        Exception: If API call fails
    """
    # Keep the LLM dependency optional: import inside.
    from openai import OpenAI  # type: ignore

    client = OpenAI(
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

    prompt = build_json_extraction_prompt(note_type, title, raw_text, available_params)

    resp = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},  # Force JSON output
    )

    json_str = resp.choices[0].message.content.strip()
    
    # Parse and validate JSON
    try:
        json_data = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"LLM did not return valid JSON: {e.msg}",
            e.doc,
            e.pos
        ) from e
    
    return json_data

