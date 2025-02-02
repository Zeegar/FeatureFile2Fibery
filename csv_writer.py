import csv

def write_to_csv(data, output_file):
    writer = csv.writer(output_file)
    writer.writerow(['Scenarios'])
    scenarios = extract_scenarios(data)
    write_scenarios(writer, scenarios)
    writer.writerow(['Feature', 'Test Case/Scenario', 'Test Step'])
    write_features_and_steps(writer, data)

def write_to_csv_from_path(data, output_file_path):
    with open(output_file_path, 'w', newline='') as file:
        write_to_csv(data, file)

def extract_scenarios(data):
    return list({row[1] for row in data})

def write_scenarios(writer, scenarios):
    for scenario in scenarios:
        writer.writerow([scenario])

def write_features_and_steps(writer, data):
    last_feature = None
    last_scenario = None

    for i, (feature, scenario, step) in enumerate(data):
        if feature == last_feature:
            feature = ''
        else:
            last_feature = feature

        if scenario == last_scenario:
            scenario = ''
        else:
            last_scenario = scenario

        writer.writerow([feature, scenario, step])

        if i + 1 < len(data) and data[i + 1][1] != last_scenario:
            writer.writerow(['', '', ''])
        elif i + 1 == len(data):
            writer.writerow(['', '', ''])
