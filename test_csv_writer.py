import unittest
from unittest.mock import mock_open, patch
from csv_writer import write_to_csv

class TestCSVWriter(unittest.TestCase):

    def test_write_to_csv(self):
        mock_data = [
            ['Feature 1', 'Scenario: Test Scenario 1', 'Given a step'],
            ['Feature 1', 'Scenario: Test Scenario 1', 'When another step'],
            ['Feature 1', 'Scenario: Test Scenario 1', 'Then a final step'],
            ['Feature 2', 'Scenario: Test Scenario 2', 'Given a step'],
            ['Feature 2', 'Scenario: Test Scenario 2', 'When another step'],
            ['Feature 2', 'Scenario: Test Scenario 2', 'Then a final step']
        ]
        expected_output = """Scenarios
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

        with patch("builtins.open", mock_open()) as mock_file:
            write_to_csv(mock_data, mock_file())
            mock_file().write.assert_called_with(expected_output)

if __name__ == "__main__":
    unittest.main()
