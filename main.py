from __future__ import annotations

from src.wiki_importer.configs.settings import default_settings
from src.wiki_importer.extractor.fandom import extract_fandom_page
from src.wiki_importer.agent.types import AgentInput
from src.wiki_importer.agent.openai_agent import run_agent
from src.wiki_importer.composer.composer import (
    download_primary_image,
    validate_required,
    compose_markdown,
    write_note,
)


def import_one(url: str, note_type: str, vault_root: str, source_name: str = "Fandom Wiki"):
    settings = default_settings(vault_root)

    page = extract_fandom_page(url, user_agent=settings.user_agent, source_name=source_name)

    agent_in = AgentInput(
        entry_type=note_type,  # e.g. "creature"
        title=page.title,
        source=page.source_name,
        source_url=page.source_url,
        raw_text=page.raw_text,
    )

    agent_out = run_agent(agent_in)

    # Choose image: prefer first candidate (infobox first by extractor design)
    image_path = None
    if page.image_candidates:
        image_path = download_primary_image(settings, agent_out.entry_type, page.title, page.image_candidates[0].url)
        agent_out.frontmatter["image"] = image_path

    # enforce note_type in frontmatter
    agent_out.frontmatter["note_type"] = agent_out.entry_type

    validate_required(settings, agent_out.entry_type, agent_out.frontmatter)

    md = compose_markdown(agent_out.frontmatter, agent_out.content)
    out_path = write_note(settings, agent_out.entry_type, page.title, md)

    print(f"Wrote: {out_path}")
    if image_path:
        print(f"Image: {image_path}")


if __name__ == "__main__":
    import_one(
        url="https://forgottenrealms.fandom.com/wiki/Mind_flayer",
        note_type="creature",
        vault_root="/path/to/your/obsidian/vault",
        source_name="Forgotten Realms Wiki",
    )

