"""
Test runner that executes test queries and validates results.
"""

import logging
import json
from typing import Dict, Any, List, Optional
from datetime import datetime

from src.agents.tool_augmenter import create_tool_augmenter
from tests.test_config import TestCase, TEST_CASES
from tests.fact_validator import FactValidator

logger = logging.getLogger(__name__)


class TestRunner:
    """
    Runs test cases and validates results.
    """
    
    def __init__(
        self,
        agent_model: str = "openai/gpt-4o",
        validator_model: str = "openai/gpt-4o",
        agent_temperature: float = 0.3,
        validator_temperature: float = 0.0,
        api_key: Optional[str] = None
    ):
        """
        Initialize the test runner.
        
        :param agent_model: Model to use for the agent
        :param validator_model: Model to use for fact validation
        :param agent_temperature: Temperature for agent
        :param validator_temperature: Temperature for validator (should be 0.0)
        :param api_key: OpenRouter API key
        """
        self.agent = create_tool_augmenter(model=agent_model, temperature=agent_temperature, api_key=api_key)
        self.validator = FactValidator(model=validator_model, temperature=validator_temperature, api_key=api_key)
    
    def _check_entity_expectations(
        self,
        test_case: TestCase,
        result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Check if expected entities were found.
        
        :param test_case: Test case definition
        :param result: Agent result
        :return: Entity validation results
        """
        if not test_case.expected_entities:
            return {
                "passed": True,
                "found_entities": [],
                "missing_entities": [],
                "message": "No entity expectations defined"
            }
        
        # Extract entities mentioned in the answer and tool calls
        answer = result.get("answer", "").lower()
        tool_calls = result.get("tool_calls", [])
        
        found_entities = []
        missing_entities = []
        
        for expected_entity in test_case.expected_entities:
            entity_lower = expected_entity.lower()
            
            # Check if entity is mentioned in answer
            if entity_lower in answer:
                found_entities.append(expected_entity)
                continue
            
            # Check if entity was retrieved via tool calls
            found_in_tools = False
            for call in tool_calls:
                tool_input = call.get("tool_input", {})
                result_text = str(call.get("result", "")).lower()
                
                # Check if entity name appears in tool input or result
                if entity_lower in str(tool_input).lower() or entity_lower in result_text:
                    found_entities.append(expected_entity)
                    found_in_tools = True
                    break
            
            if not found_in_tools:
                missing_entities.append(expected_entity)
        
        passed = len(missing_entities) == 0
        
        return {
            "passed": passed,
            "found_entities": found_entities,
            "missing_entities": missing_entities,
            "message": f"Found {len(found_entities)}/{len(test_case.expected_entities)} expected entities"
        }
    
    def run_test_case(self, test_case: TestCase) -> Dict[str, Any]:
        """
        Run a single test case and return results.
        
        :param test_case: Test case to run
        :return: Test results dictionary
        """
        if test_case.skip:
            return {
                "test_case": test_case.query,
                "skipped": True,
                "message": "Test case marked as skipped"
            }
        
        logger.info(f"Running test case: {test_case.query}")
        
        start_time = datetime.now()
        
        # Run the agent
        try:
            agent_result = self.agent(test_case.query)
        except Exception as e:
            logger.error(f"Error running agent for test case '{test_case.query}': {e}")
            return {
                "test_case": test_case.query,
                "passed": False,
                "error": str(e),
                "agent_success": False
            }
        
        agent_time = (datetime.now() - start_time).total_seconds()
        
        # Validate facts using counter-factual validator
        fact_validation = None
        if agent_result.get("success") and agent_result.get("tool_calls"):
            try:
                fact_validation = self.validator.validate(
                    query=test_case.query,
                    response=agent_result.get("answer", ""),
                    tool_calls=agent_result.get("tool_calls", [])
                )
            except Exception as e:
                logger.error(f"Error during fact validation: {e}")
                fact_validation = {
                    "error": str(e),
                    "confidence": 0.0
                }
        
        # Check entity expectations
        entity_validation = self._check_entity_expectations(test_case, agent_result)
        
        # Determine overall pass/fail
        passed = (
            agent_result.get("success", False) and
            entity_validation["passed"] and
            (fact_validation is None or fact_validation.get("confidence", 0.0) >= 0.7)
        )
        
        total_time = (datetime.now() - start_time).total_seconds()
        
        return {
            "test_case": test_case.query,
            "description": test_case.description,
            "passed": passed,
            "agent_success": agent_result.get("success", False),
            "agent_answer": agent_result.get("answer", ""),
            "tool_calls_count": len(agent_result.get("tool_calls", [])),
            "entity_validation": entity_validation,
            "fact_validation": fact_validation,
            "timing": {
                "agent_time_seconds": agent_time,
                "total_time_seconds": total_time
            }
        }
    
    def run_all_tests(self, test_cases: Optional[List[TestCase]] = None) -> Dict[str, Any]:
        """
        Run all test cases and return summary results.
        
        :param test_cases: Optional list of test cases (defaults to TEST_CASES)
        :return: Summary results dictionary
        """
        if test_cases is None:
            test_cases = TEST_CASES
        
        logger.info(f"Running {len(test_cases)} test cases")
        
        results = []
        passed_count = 0
        failed_count = 0
        skipped_count = 0
        
        for test_case in test_cases:
            result = self.run_test_case(test_case)
            results.append(result)
            
            if result.get("skipped"):
                skipped_count += 1
            elif result.get("passed"):
                passed_count += 1
            else:
                failed_count += 1
        
        total_time = sum(r.get("timing", {}).get("total_time_seconds", 0) for r in results)
        
        return {
            "summary": {
                "total": len(test_cases),
                "passed": passed_count,
                "failed": failed_count,
                "skipped": skipped_count,
                "total_time_seconds": total_time
            },
            "results": results
        }
    
    def print_results(self, results: Dict[str, Any]):
        """
        Print test results in a readable format.
        
        :param results: Results dictionary from run_all_tests
        """
        summary = results["summary"]
        test_results = results["results"]
        
        print("\n" + "="*80)
        print("TEST RESULTS SUMMARY")
        print("="*80)
        print(f"Total Tests: {summary['total']}")
        print(f"Passed: {summary['passed']} ✓")
        print(f"Failed: {summary['failed']} ✗")
        print(f"Skipped: {summary['skipped']} ⊘")
        print(f"Total Time: {summary['total_time_seconds']:.2f}s")
        print("="*80)
        
        for i, result in enumerate(test_results, 1):
            print(f"\n--- Test {i}: {result['test_case']} ---")
            
            if result.get("skipped"):
                print("SKIPPED")
                continue
            
            status = "PASSED ✓" if result.get("passed") else "FAILED ✗"
            print(f"Status: {status}")
            
            if result.get("description"):
                print(f"Description: {result['description']}")
            
            # Agent status
            if result.get("agent_success"):
                print(f"Agent: Success ({result.get('tool_calls_count', 0)} tool calls)")
            else:
                print(f"Agent: Failed")
                if result.get("error"):
                    print(f"  Error: {result['error']}")
            
            # Entity validation
            entity_val = result.get("entity_validation", {})
            if entity_val:
                print(f"Entity Validation: {'PASSED' if entity_val.get('passed') else 'FAILED'}")
                if entity_val.get("found_entities"):
                    print(f"  Found: {', '.join(entity_val['found_entities'])}")
                if entity_val.get("missing_entities"):
                    print(f"  Missing: {', '.join(entity_val['missing_entities'])}")
            
            # Fact validation
            fact_val = result.get("fact_validation")
            if fact_val:
                confidence = fact_val.get("confidence", 0.0)
                print(f"Fact Validation: Confidence {confidence:.2f}")
                if fact_val.get("unsupported_facts"):
                    print(f"  Unsupported Facts ({len(fact_val['unsupported_facts'])}):")
                    for fact in fact_val["unsupported_facts"][:3]:  # Show first 3
                        print(f"    - {fact}")
                    if len(fact_val["unsupported_facts"]) > 3:
                        print(f"    ... and {len(fact_val['unsupported_facts']) - 3} more")
            
            # Timing
            timing = result.get("timing", {})
            if timing:
                print(f"Time: {timing.get('total_time_seconds', 0):.2f}s")
            
            print()


def main():
    """Main entry point for running tests."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Run agent test suite')
    parser.add_argument('--agent-model', type=str, default="openai/gpt-4o",
                        help='Model for the agent')
    parser.add_argument('--validator-model', type=str, default="openai/gpt-4o",
                        help='Model for fact validation')
    parser.add_argument('--agent-temp', type=float, default=0.3,
                        help='Temperature for agent')
    parser.add_argument('--validator-temp', type=float, default=0.0,
                        help='Temperature for validator')
    parser.add_argument('--output', type=str, help='Output JSON file for results')
    parser.add_argument('--test-index', type=int, help='Run a specific test by index (0-based)')
    args = parser.parse_args()
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Create test runner
    runner = TestRunner(
        agent_model=args.agent_model,
        validator_model=args.validator_model,
        agent_temperature=args.agent_temp,
        validator_temperature=args.validator_temp
    )
    
    # Run tests
    if args.test_index is not None:
        # Run single test
        if 0 <= args.test_index < len(TEST_CASES):
            test_case = TEST_CASES[args.test_index]
            result = runner.run_test_case(test_case)
            runner.print_results({
                "summary": {
                    "total": 1,
                    "passed": 1 if result.get("passed") else 0,
                    "failed": 0 if result.get("passed") else 1,
                    "skipped": 1 if result.get("skipped") else 0,
                    "total_time_seconds": result.get("timing", {}).get("total_time_seconds", 0)
                },
                "results": [result]
            })
            
            if args.output:
                with open(args.output, 'w') as f:
                    json.dump({"results": [result]}, f, indent=2, default=str)
        else:
            print(f"Error: Test index {args.test_index} out of range (0-{len(TEST_CASES)-1})")
    else:
        # Run all tests
        results = runner.run_all_tests()
        runner.print_results(results)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(results, f, indent=2, default=str)


if __name__ == '__main__':
    main()

