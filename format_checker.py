def check_formatting(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    errors = []
    scenario_outline = False
    examples_table = False

    for i, line in enumerate(lines):
        line = line.strip()
        if not any(line.startswith(keyword) for keyword in
                   ['Feature:', ' ', '', '@', 'Scenario:',
                    'Scenario Outline:', 'Developer Task:', 'Given', 'And',
                    'When', 'Then']):
            errors.append(f"Formatting error on line {i + 1}: {line}")
        if line.startswith('Scenario Outline:'):
            scenario_outline = True
            examples_table = False
        if line.startswith('Examples:'):
            examples_table = True
        if line.startswith('|') and scenario_outline and not examples_table:
            errors.append(f"Formatting error on line {i + 1}: 'Scenario Outline' must be followed by an examples table with lines 'Examples:' and '|'")

    if errors:
        return "\n".join(errors)
    else:
        return "Formatting Ok"
