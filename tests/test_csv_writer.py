import io
import csv
import unittest
import tempfile
import os
from csv_writer import write_to_csv

class TestCsvWriter(unittest.TestCase):
    def test_write_to_csv(self):
        data = [
            ['Feature 1', 'Scenario: Test Scenario 1', 'Given a step'],
            ['Feature 1', 'Scenario: Test Scenario 1', 'When another step'],
            ['Feature 1', 'Scenario: Test Scenario 1', 'Then a final step'],
            ['Feature 2', 'Scenario: Test Scenario 2', 'Given a step'],
            ['Feature 2', 'Scenario: Test Scenario 2', 'When another step'],
            ['Feature 2', 'Scenario: Test Scenario 2', 'Then a final step']
        ]
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
        try:
            write_to_csv(data, temp_file_path)
            with open(temp_file_path, 'r') as file:
                output = file.read()
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
            self.assertEqual(output, expected_output)
        finally:
            os.remove(temp_file_path)

if __name__ == "__main__":
    unittest.main()
