# Wiki Importer

A Python package for importing wiki pages into Obsidian notes for D&D campaigns. Extracts content from Fandom wikis, processes it with AI to extract structured data, and composes markdown notes with proper frontmatter.

## Overview

The wiki importer consists of several modules:

- **Extractor** - Scrapes wiki pages and extracts content
- **Agent** - Uses LLM to extract structured data from wiki content
- **Composer** - Builds markdown notes with YAML frontmatter

## Quick Start

### Single Page Import

Import a single wiki page:

```bash
python -m src.wiki_importer.import_complete https://spelljammer.fandom.com/wiki/Airslug --type creature
```

With image download:

```bash
python -m src.wiki_importer.import_complete https://spelljammer.fandom.com/wiki/Airslug --type creature --download-image
```

### Batch Import

Create a batch file (`batch.json`):

```json
[
  ["https://spelljammer.fandom.com/wiki/Airslug", "creature"],
  ["https://spelljammer.fandom.com/wiki/Bral", "location"],
  ["https://forgottenrealms.fandom.com/wiki/Mind_flayer", "creature"]
]
```

Or text format (`batch.txt`):

```
https://spelljammer.fandom.com/wiki/Airslug|creature
https://spelljammer.fandom.com/wiki/Bral|location
https://forgottenrealms.fandom.com/wiki/Mind_flayer|creature
```

Run batch import:

```bash
python -m src.wiki_importer.batch_import batch.json
```

## Scripts

### `import_complete.py`

Complete workflow: extract → process → compose in one command.

**Usage:**
```bash
python -m src.wiki_importer.import_complete <url> --type <type> [options]
```

**Arguments:**
- `url` - URL of the wiki page to import
- `--type` - Note type: `creature`, `faction`, `location`, `character`, `item`, or `entry`
- `--vault-root` - Path to Obsidian vault (default: `content/1 Keepers' Compendium`)
- `--source-name` - Override source name (auto-detected from URL)
- `--download-image` - Download images if available
- `--save-intermediates` - Save intermediate .txt and .json files

**Examples:**
```bash
# Basic import
python -m src.wiki_importer.import_complete https://spelljammer.fandom.com/wiki/Airslug --type creature

# With image download
python -m src.wiki_importer.import_complete https://spelljammer.fandom.com/wiki/Airslug --type creature --download-image

# Custom vault root
python -m src.wiki_importer.import_complete https://spelljammer.fandom.com/wiki/Airslug --type creature --vault-root ./custom/path
```

### `batch_import.py`

Process multiple wiki pages from a batch file.

**Usage:**
```bash
python -m src.wiki_importer.batch_import <batch_file> [options]
```

**Arguments:**
- `batch_file` - Path to batch file (JSON or text format)
- `--vault-root` - Path to Obsidian vault (default: `content/1 Keepers' Compendium`)
- `--download-image` - Download images if available
- `--save-intermediates` - Save intermediate files
- `--stop-on-error` - Stop processing on first error (default: continue)

**Examples:**
```bash
# Process batch file
python -m src.wiki_importer.batch_import batch.json

# With options
python -m src.wiki_importer.batch_import batch.json --download-image --save-intermediates

# Stop on first error
python -m src.wiki_importer.batch_import batch.json --stop-on-error
```

### `import_wiki.py`

Extract wiki page and save to .txt file (no AI processing).

**Usage:**
```bash
python -m src.wiki_importer.import_wiki <url> [--source-name NAME]
```

**Example:**
```bash
python -m src.wiki_importer.import_wiki https://spelljammer.fandom.com/wiki/Airslug
```

### `process_page.py`

Process a pre-extracted .txt file with AI to generate structured JSON.

**Usage:**
```bash
python -m src.wiki_importer.process_page <txt_file> --note-type <type>
```

**Example:**
```bash
python -m src.wiki_importer.process_page outputs/airslug_20251216_200717.txt --note-type creature
```

### `compose_note.py`

Compose markdown note from structured JSON file.

**Usage:**
```bash
python -m src.wiki_importer.compose_note <json_file> --vault-root <path> [--download-image]
```

**Example:**
```bash
python -m src.wiki_importer.compose_note outputs/airslug_20251216_200717.json --vault-root ./content --download-image
```

## Note Types

Supported note types and their available parameters:

### Creature
- `creature_type`, `size`, `usual_alignment`, `origin`, `known_locations`, `appears_in`, `image`

### Faction
- `parent`, `location`, `faction_type`, `alignment`, `leader`, `appears_in`

### Location
- `location_type`, `parent`, `appears_in`, `image`

### Character
- `origin`, `class`, `race`, `known_locations`, `factions`, `alignment`, `appears_in`, `image`

### Item
- `relates_to`, `item_type`, `item_rarity`

### Entry
- `entry_type`, `relates_to`, `author`

## Output Structure

Notes are saved to:
```
vault_root/
  wiki/
    creature/
    faction/
    location/
    character/
    item/
    entry/
  assets/
    creatures/
    factions/
    locations/
    characters/
    items/
    entry/
```

## Features

- **Automatic source detection** - Detects wiki source from URL
- **Structured extraction** - AI extracts relevant parameters based on note type
- **Section summaries** - Summarizes each section of the article with markdown formatting
- **Image handling** - Downloads and links images in Obsidian format
- **Duplicate protection** - Appends "- wiki import" if file already exists
- **Batch processing** - Process multiple pages with error handling
- **Progress tracking** - Detailed progress output and results logging

## Requirements

- Python 3.10+
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `openai` - LLM API (OpenRouter compatible)
- `PyYAML` - YAML frontmatter (optional but recommended)

## Configuration

Set your OpenRouter API key in `src/secrets.py`:

```python
OPENROUTER_API_KEY = "sk-or-v1-your-key-here"
```

Or set as environment variable:
```bash
export OPENROUTER_API_KEY="sk-or-v1-your-key-here"
```

## Default Paths

- **Vault root**: `content/1 Keepers' Compendium` (relative to project root)
- **Outputs**: `src/wiki_importer/outputs/` (intermediate files)

## Notes

- Titles are automatically capitalized in frontmatter
- Image links use Obsidian format: `[[path/to/image.png]]`
- Existing files are preserved (new files get "- wiki import" suffix)
- Batch processing saves results to `{batch_file}_results.json`

