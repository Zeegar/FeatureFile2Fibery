import io
import csv
from csv_writer import write_to_csv

def test_write_to_csv():
    data = [
        ['Feature 1', 'Scenario: Test Scenario 1', 'Given a step'],
        ['Feature 1', 'Scenario: Test Scenario 1', 'When another step'],
        ['Feature 1', 'Scenario: Test Scenario 1', 'Then a final step'],
        ['Feature 2', 'Scenario: Test Scenario 2', 'Given a step'],
        ['Feature 2', 'Scenario: Test Scenario 2', 'When another step'],
        ['Feature 2', 'Scenario: Test Scenario 2', 'Then a final step']
    ]
    output = io.StringIO()
    write_to_csv(data, output)
    output.seek(0)
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
    assert output.getvalue() == expected_output
