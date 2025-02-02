import io
from gherkin_parser import parse_feature_file

def test_parse_feature_file():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = [
        ['Test Feature', '', ''],
        ['Test Feature', 'Scenario: Test Scenario', ''],
        ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
        ['Test Feature', 'Scenario: Test Scenario', 'When another step'],
        ['Test Feature', 'Scenario: Test Scenario', 'Then a final step']
    ]
    assert parse_feature_file(feature_file) == expected_output

def test_scenario_outline_followed_by_examples():
    feature_file_content = """Feature: Test Feature
Scenario Outline: Test Scenario Outline
Given a step
When another step
Then a final step
Examples:
| column 1 |
| value 1  |
| value 2  |
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = [
        ['Test Feature', '', ''],
        ['Test Feature', 'Scenario Outline: Test Scenario Outline', ''],
        ['Test Feature', 'Scenario Outline: Test Scenario Outline', 'Given a step'],
        ['Test Feature', 'Scenario Outline: Test Scenario Outline', 'When another step'],
        ['Test Feature', 'Scenario Outline: Test Scenario Outline', 'Then a final step'],
        ['Test Feature', 'Scenario Outline: Test Scenario Outline', 'Examples:'],
        ['Test Feature', 'Scenario Outline: Test Scenario Outline', '| column 1 |'],
        ['Test Feature', 'Scenario Outline: Test Scenario Outline', '| value 1  |'],
        ['Test Feature', 'Scenario Outline: Test Scenario Outline', '| value 2  |']
    ]
    assert parse_feature_file(feature_file) == expected_output

def test_invalid_gherkin_syntax():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Given a step
Invalid line
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = [
        ['Test Feature', '', ''],
        ['Test Feature', 'Scenario: Test Scenario', ''],
        ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
        ['Test Feature', 'Scenario: Test Scenario', 'Invalid Gherkin syntax at line 4: Invalid line']
    ]
    assert parse_feature_file(feature_file) == expected_output

def test_missing_elements():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = [
        ['Test Feature', '', ''],
        ['Test Feature', 'Scenario: Test Scenario', '']
    ]
    assert parse_feature_file(feature_file) == expected_output

def test_incorrect_formatting():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
1Scenario: Different formatting
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = [
        ['Test Feature', '', ''],
        ['Test Feature', 'Scenario: Test Scenario', ''],
        ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
        ['Test Feature', 'Scenario: Test Scenario', 'When another step'],
        ['Test Feature', 'Scenario: Test Scenario', 'Then a final step'],
        ['Test Feature', 'Scenario: Test Scenario', 'Invalid Gherkin syntax at line 6: 1Scenario: Different formatting']
    ]
    assert parse_feature_file(feature_file) == expected_output
