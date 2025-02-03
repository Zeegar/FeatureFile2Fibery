import io
import unittest
from format_checker import check_formatting

class TestFormatChecker(unittest.TestCase):
    def test_check_formatting(self):
        feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
Invalid line
"""
        feature_file = io.StringIO(feature_file_content)
        expected_output = ["Formatting error on line 6: Invalid line"]
        self.assertEqual(check_formatting(feature_file), expected_output)

if __name__ == "__main__":
    unittest.main()
