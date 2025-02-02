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
