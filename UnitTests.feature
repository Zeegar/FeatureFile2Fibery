Feature: Unit Tests

Scenario: Test parse_feature_file function
Given a feature file with the following content:
"""
Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
"""
When the parse_feature_file function is called
Then the output should be:
"""
[
    ['Test Feature', '', ''],
    ['Test Feature', 'Scenario: Test Scenario', ''],
    ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
    ['Test Feature', 'Scenario: Test Scenario', 'When another step'],
    ['Test Feature', 'Scenario: Test Scenario', 'Then a final step']
]
"""

Scenario: Test write_to_csv function
Given the following data:
"""
[
    ['Feature 1', 'Scenario: Test Scenario 1', 'Given a step'],
    ['Feature 1', 'Scenario: Test Scenario 1', 'When another step'],
    ['Feature 1', 'Scenario: Test Scenario 1', 'Then a final step'],
    ['Feature 2', 'Scenario: Test Scenario 2', 'Given a step'],
    ['Feature 2', 'Scenario: Test Scenario 2', 'When another step'],
    ['Feature 2', 'Scenario: Test Scenario 2', 'Then a final step']
]
"""
When the write_to_csv function is called
Then the output CSV file should contain:
"""
Scenarios
Scenario: Test Scenario 1
Scenario: Test Scenario 2
Feature,Test Case/Scenario,Test Step
Feature 1,Scenario: Test Scenario 1,Given a step
,,When another step
,,Then a final step
,,
Feature 2,Scenario: Test Scenario 2,Given a step
,,When another step
,,Then a final step
,,
"""

Scenario: Test check_formatting function
Given a feature file with the following content:
"""
Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
Invalid line
"""
When the check_formatting function is called
Then the output should be:
"""
Formatting error on line 6: Invalid line
"""

Scenario: Test main function
Given a feature file with the following content:
"""
Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
"""
When the main function is called
Then the output CSV file should contain:
"""
Scenarios
Scenario: Test Scenario
Feature,Test Case/Scenario,Test Step
Test Feature,Scenario: Test Scenario,Given a step
,,When another step
,,Then a final step
,,
"""

Scenario: Test missing Feature keyword
Given a feature file with the following content:
"""
Scenario: Test Scenario
Given a step
When another step
Then a final step
"""
When the parse_feature_file function is called
Then the output should be:
"""
[]
"""

Scenario: Test missing Scenario keyword
Given a feature file with the following content:
"""
Feature: Test Feature
Given a step
When another step
Then a final step
"""
When the parse_feature_file function is called
Then the output should be:
"""
[
    ['Test Feature', '', '']
]
"""

Scenario: Test invalid step keywords
Given a feature file with the following content:
"""
Feature: Test Feature
Scenario: Test Scenario
Giben a step
Whan another step
Then a final step
"""
When the parse_feature_file function is called
Then the output should be:
"""
[
    ['Test Feature', '', ''],
    ['Test Feature', 'Scenario: Test Scenario', '']
]
"""

Scenario: Test empty lines and lines with only whitespace
Given a feature file with the following content:
"""
Feature: Test Feature

Scenario: Test Scenario

Given a step

When another step

Then a final step

"""
When the parse_feature_file function is called
Then the output should be:
"""
[
    ['Test Feature', '', ''],
    ['Test Feature', 'Scenario: Test Scenario', ''],
    ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
    ['Test Feature', 'Scenario: Test Scenario', 'When another step'],
    ['Test Feature', 'Scenario: Test Scenario', 'Then a final step']
]
"""

Scenario: Test missing Scenario Outline keyword
Given a feature file with the following content:
"""
Feature: Test Feature
Scenario Outline: Test Scenario Outline
Given a step
When another step
Then a final step
Examples:
| column 1 |
| value 1  |
| value 2  |
"""
When the parse_feature_file function is called
Then the output should be:
"""
[
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
"""
