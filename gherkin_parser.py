def parse_feature_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    features = []
    current_feature = None
    current_scenario = None

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
        elif any(line.startswith(keyword) for keyword in
                 ['Given', 'When', 'Then', 'And', 'Examples', '|']):
            if current_feature and current_scenario:
                features.append([current_feature, current_scenario, line])
        elif line:
            print(f"Invalid Gherkin syntax at line {line_number}: {line}")

    return features


def check_formatting(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    errors = []
    for i, line in enumerate(lines):
        line = line.strip()
        if not any(line.startswith(keyword) for keyword in
                   ['Feature:', ' ', '', '@', 'Scenario:',
                    'Scenario Outline:', 'Developer Task:', 'Given', 'And',
                    'When', 'Then']):
            errors.append(f"Formatting error on line {i + 1}: {line}")

    if errors:
        return "\n".join(errors)
    else:
        return "Formatting Ok"
