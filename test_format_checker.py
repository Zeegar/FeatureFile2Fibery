import unittest
from unittest.mock import mock_open, patch
from format_checker import check_formatting

class TestFormatChecker(unittest.TestCase):

    def test_check_formatting(self):
        mock_feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
Invalid line
"""
        expected_output = "Formatting error on line 6: Invalid line"

        with patch("builtins.open", mock_open(read_data=mock_feature_file_content)):
            with open("mock_feature_file.feature", "r") as mock_file:
                result = check_formatting(mock_file)
                self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()
