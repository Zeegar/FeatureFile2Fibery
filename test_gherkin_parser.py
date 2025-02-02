import unittest
from unittest.mock import mock_open, patch
from gherkin_parser import parse_feature_file

class TestGherkinParser(unittest.TestCase):

    def test_parse_feature_file(self):
        mock_feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
"""
        expected_output = [
            ['Test Feature', '', ''],
            ['Test Feature', 'Scenario: Test Scenario', ''],
            ['Test Feature', 'Scenario: Test Scenario', 'Given a step'],
            ['Test Feature', 'Scenario: Test Scenario', 'When another step'],
            ['Test Feature', 'Scenario: Test Scenario', 'Then a final step']
        ]

        with patch("builtins.open", mock_open(read_data=mock_feature_file_content)):
            with open("mock_feature_file.feature", "r") as mock_file:
                result = parse_feature_file(mock_file)
                self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
