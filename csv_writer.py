import csv

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Scenarios'])
        scenarios = extract_scenarios(data)
        write_scenarios(writer, scenarios)
        writer.writerow(['Feature', 'Test Case/Scenario', 'Test Step'])
        write_features_and_steps(writer, data)

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
