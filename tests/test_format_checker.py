import io
from format_checker import check_formatting

def test_check_formatting():
    feature_file_content = """Feature: Test Feature
Scenario: Test Scenario
Given a step
When another step
Then a final step
Invalid line
"""
    feature_file = io.StringIO(feature_file_content)
    expected_output = "Formatting error on line 6: Invalid line"
    assert check_formatting(feature_file) == expected_output
