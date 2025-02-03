import re

def check_formatting(feature_file):
    errors = []
    valid_keywords = ['Feature:', 'Scenario:', 'Scenario Outline:', 'Developer Task:', 'Given', 'When', 'Then', 'And', 'Examples', '|']

    for line_number, line in enumerate(feature_file, start=1):
        line = line.lstrip()
        if not any(line.startswith(keyword) for keyword in valid_keywords) and line:
            errors.append(f"Formatting error on line {line_number}: {line}")

    return errors
