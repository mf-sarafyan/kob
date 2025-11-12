"""
Example usage of the test framework.

This script demonstrates how to use the test framework programmatically.
"""

from tests.test_runner import TestRunner
from tests.test_config import TestCase, TEST_CASES

def main():
    """Example: Run a single test case."""
    
    # Create test runner
    runner = TestRunner(
        agent_model="openai/gpt-4o",
        validator_model="openai/gpt-4o",
        agent_temperature=0.3,
        validator_temperature=0.0
    )
    
    # Run a single test case
    test_case = TEST_CASES[0]  # First test case
    result = runner.run_test_case(test_case)
    
    print(f"\nTest: {result['test_case']}")
    print(f"Passed: {result['passed']}")
    print(f"Agent Success: {result['agent_success']}")
    
    if result.get('entity_validation'):
        ev = result['entity_validation']
        print(f"Entity Validation: {'PASSED' if ev['passed'] else 'FAILED'}")
        print(f"  Found: {ev['found_entities']}")
        print(f"  Missing: {ev['missing_entities']}")
    
    if result.get('fact_validation'):
        fv = result['fact_validation']
        print(f"Fact Validation Confidence: {fv.get('confidence', 0.0):.2f}")
        if fv.get('unsupported_facts'):
            print(f"Unsupported Facts: {fv['unsupported_facts']}")


if __name__ == '__main__':
    main()

