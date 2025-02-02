import re
from difflib import get_close_matches

def parse_feature_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    features = []
    current_feature = None
    current_scenario = None
    scenario_outline = False
    examples_table = False
    errors = []
    warnings = []
    valid_keywords = ['Feature:', 'Scenario:', 'Scenario Outline:', 'Developer Task:', 'Given', 'When', 'Then', 'And', 'Examples', '|']

    for line_number, line in enumerate(lines, start=1):
        line = line.lstrip()
        line = line.rstrip()
        if line.startswith('Feature:'):
            current_feature = line[len('Feature:'):].strip()
            features.append([current_feature, '', ''])
        elif (line.startswith('Scenario:') or
              line.startswith('Scenario Outline:') or
              line.startswith('Developer Task:')):
            current_scenario = line.strip()
            if current_feature and not any(f[0] == current_feature for f in features):
                features.append([current_feature, '', ''])
            if current_feature and current_scenario:
                features.append([current_feature, current_scenario, ''])
            if line.startswith('Scenario Outline:'):
                scenario_outline = True
                examples_table = False
        elif any(line.startswith(keyword) for keyword in valid_keywords):
            if current_feature and current_scenario:
                features.append([current_feature, current_scenario, line])
            if line.startswith('Examples:'):
                examples_table = True
            if line.startswith('|') and scenario_outline and not examples_table:
                errors.append(f"Invalid Gherkin syntax at line {line_number}: 'Scenario Outline' must be followed by an examples table with lines 'Examples:' and '|'")
        elif line:
            closest_match = find_closest_match(line, valid_keywords)
            if closest_match:
                user_input = input(f"Did you mean '{closest_match}' instead of '{line}'? (yes/no): ")
                if user_input.lower() == 'yes':
                    update_feature_file(file_path, line_number, closest_match)
                    return parse_feature_file(file_path)
            errors.append(f"Invalid Gherkin syntax at line {line_number}: {line}")

    return {
        'features': features,
        'errors': errors,
        'warnings': warnings,
        'valid_keywords': valid_keywords
    }

def find_closest_match(line, valid_keywords):
    matches = get_close_matches(line, valid_keywords)
    return matches[0] if matches else None

def update_feature_file(file_path, line_number, new_line):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines[line_number - 1] = new_line + '\n'

    with open(file_path, 'w') as file:
        file.writelines(lines)
