def parse_feature_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    features = []
    current_feature = None
    current_scenario = None
    scenario_outline = False
    examples_table = False

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
        elif any(line.startswith(keyword) for keyword in
                 ['Given', 'When', 'Then', 'And', 'Examples', '|']):
            if current_feature and current_scenario:
                features.append([current_feature, current_scenario, line])
            if line.startswith('Examples:'):
                examples_table = True
            if line.startswith('|') and scenario_outline and not examples_table:
                print(f"Invalid Gherkin syntax at line {line_number}: 'Scenario Outline' must be followed by an examples table with lines 'Examples:' and '|'")
        elif line:
            print(f"Invalid Gherkin syntax at line {line_number}: {line}")

    return features
