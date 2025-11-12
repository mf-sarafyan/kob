# Agent Test Suite

This directory contains a comprehensive test environment for validating the tool augmenter agent.

## Structure

- `test_config.py`: Defines test cases with queries and expected outcomes
- `test_runner.py`: Executes test cases and collects results
- `fact_validator.py`: Counter-factual validator that checks if facts in responses are supported by context

## Features

### 1. Test Case Configuration

Test cases are defined in `test_config.py` with:
- **query**: The test query to run
- **expected_entities**: List of entity names that should be found/mentioned
- **expected_facts**: List of specific facts that should be present (future enhancement)
- **description**: Human-readable description of what the test validates

### 2. Entity Validation

The test runner checks if expected entities are:
- Mentioned in the assistant's response
- Retrieved via tool calls (entity_details, search_entity, etc.)

### 3. Counter-Factual Fact Validation

The fact validator uses an LLM to analyze whether facts mentioned in the assistant's response are actually supported by the context retrieved from tool calls. This helps detect:
- Hallucinations (facts made up by the assistant)
- General knowledge leakage (using D&D knowledge not in the knowledge base)
- Unsupported inferences

## Usage

### Run All Tests

```bash
python -m tests.test_runner
```

### Run a Specific Test

```bash
python -m tests.test_runner --test-index 0
```

### Run with Custom Models

```bash
python -m tests.test_runner --agent-model "openai/gpt-4o" --validator-model "openai/gpt-4o"
```

### Save Results to JSON

```bash
python -m tests.test_runner --output results.json
```

### Command Line Options

- `--agent-model`: Model for the agent (default: "openai/gpt-4o")
- `--validator-model`: Model for fact validation (default: "openai/gpt-4o")
- `--agent-temp`: Temperature for agent (default: 0.3)
- `--validator-temp`: Temperature for validator (default: 0.0)
- `--output`: Output JSON file for results
- `--test-index`: Run a specific test by index (0-based)

## Adding New Test Cases

Edit `test_config.py` and add a new `TestCase` to the `TEST_CASES` list:

```python
TestCase(
    query="Your test query here",
    expected_entities=["Entity1", "Entity2"],
    expected_facts=["Fact that should be present"],
    description="What this test validates"
)
```

## Test Results

The test runner provides:
- **Summary**: Total tests, passed/failed/skipped counts, total time
- **Per-test results**: 
  - Agent success status
  - Entity validation (found/missing entities)
  - Fact validation (confidence score, unsupported facts)
  - Timing information

## Fact Validation Details

The fact validator:
1. Extracts context from all tool call results
2. Sends the query, response, and context to an LLM validator
3. Returns:
   - `supported_facts`: Facts that are backed by context
   - `unsupported_facts`: Facts that appear to be made up or not in context
   - `confidence`: Overall confidence score (0.0 to 1.0)
   - `summary`: Brief summary of validation results

A test passes if:
- Agent execution succeeds
- All expected entities are found
- Fact validation confidence >= 0.7

