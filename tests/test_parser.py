import io
from gherkin_parser import parse_feature_file, find_closest_match, update_feature_file

def test_parse_feature_file():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = {
        'features': [
            ['Test Feature', '', ''],
            ['Test Feature', 'Scenario: Test Scenario', ''],
            ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
            ['Test Feature', 'Scenario: Test Scenario', 'When another step'],
            ['Test Feature', 'Scenario: Test Scenario', 'Then a final step']
        ],
        'errors': [],
        'warnings': []
    }
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

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
    expected_output = {
        'features': [
            ['Test Feature', '', ''],
            ['Test Feature', 'Scenario Outline: Test Scenario Outline', ''],
            ['Test Feature', 'Scenario Outline: Test Scenario Outline', 'Given a step'],
            ['Test Feature', 'Scenario Outline: Test Scenario Outline', 'When another step'],
            ['Test Feature', 'Scenario Outline: Test Scenario Outline', 'Then a final step'],
            ['Test Feature', 'Scenario Outline: Test Scenario Outline', 'Examples:'],
            ['Test Feature', 'Scenario Outline: Test Scenario Outline', '| column 1 |'],
            ['Test Feature', 'Scenario Outline: Test Scenario Outline', '| value 1  |'],
            ['Test Feature', 'Scenario Outline: Test Scenario Outline', '| value 2  |']
        ],
        'errors': [],
        'warnings': []
    }
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

def test_missing_feature_keyword():
    feature_file_content = """Scenario: Test Scenario
Given a step
When another step
Then a final step
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = {
        'features': [],
        'errors': ["Invalid Gherkin syntax at line 1: Scenario: Test Scenario"],
        'warnings': []
    }
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

def test_missing_scenario_keyword():
    feature_file_content = """Feature: Test Feature
Given a step
When another step
Then a final step
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = {
        'features': [['Test Feature', '', '']],
        'errors': [
            "Invalid Gherkin syntax at line 2: Given a step",
            "Invalid Gherkin syntax at line 3: When another step",
            "Invalid Gherkin syntax at line 4: Then a final step"
        ],
        'warnings': []
    }
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

def test_invalid_step_keywords():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Giben a step
Whan another step
Then a final step
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = {
        'features': [
            ['Test Feature', '', ''],
            ['Test Feature', 'Scenario: Test Scenario', '']
        ],
        'errors': [
            "Invalid Gherkin syntax at line 3: Giben a step",
            "Invalid Gherkin syntax at line 4: Whan another step"
        ],
        'warnings': []
    }
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

def test_empty_lines_and_whitespace():
    feature_file_content = """Feature: Test Feature

Scenario: Test Scenario

Given a step

When another step

Then a final step

"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = {
        'features': [
            ['Test Feature', '', ''],
            ['Test Feature', 'Scenario: Test Scenario', ''],
            ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
            ['Test Feature', 'Scenario: Test Scenario', 'When another step'],
            ['Test Feature', 'Scenario: Test Scenario', 'Then a final step']
        ],
        'errors': [],
        'warnings': []
    }
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

def test_missing_scenario_outline_keyword():
    feature_file_content = """Feature: Test Feature
Given a step
When another step
Then a final step
Examples:
| column 1 |
| value 1  |
| value 2  |
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = {
        'features': [['Test Feature', '', '']],
        'errors': [
            "Invalid Gherkin syntax at line 2: Given a step",
            "Invalid Gherkin syntax at line 3: When another step",
            "Invalid Gherkin syntax at line 4: Then a final step",
            "Invalid Gherkin syntax at line 5: Examples:",
            "Invalid Gherkin syntax at line 6: | column 1 |",
            "Invalid Gherkin syntax at line 7: | value 1  |",
            "Invalid Gherkin syntax at line 8: | value 2  |"
        ],
        'warnings': []
    }
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

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
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

def test_missing_elements():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = [
        ['Test Feature', '', ''],
        ['Test Feature', 'Scenario: Test Scenario', '']
    ]
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

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
    assert parse_feature_file(feature_file)['features'] == expected_output['features']

def test_find_closest_match():
    line = "Giben a step"
    valid_keywords = ['Feature:', 'Scenario:', 'Scenario Outline:', 'Developer Task:', 'Given', 'When', 'Then', 'And', 'Examples', '|']
    expected_output = "Given"
    assert find_closest_match(line, valid_keywords) == expected_output

def test_update_feature_file():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Giben a step
When another step
Then a final step
"""
    feature_file = io.StringIO(feature_file_content)
    update_feature_file(feature_file, 3, "Given a step")
    expected_output = """Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
"""
    assert feature_file.getvalue() == expected_output

def test_inspect_feature():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Giben a step
When another step
Then a final step
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = {
        'features': [
            ['Test Feature', '', ''],
            ['Test Feature', 'Scenario: Test Scenario', ''],
            ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
            ['Test Feature', 'Scenario: Test Scenario', 'When another step'],
            ['Test Feature', 'Scenario: Test Scenario', 'Then a final step']
        ],
        'errors': [],
        'warnings': []
    }
    assert parse_feature_file(feature_file)['features'] == expected_output['features']
