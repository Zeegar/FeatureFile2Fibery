import sys
import re
from gherkin_parser import parse_feature_file, find_closest_match, update_feature_file, create_backup, restore_backup
from csv_writer import write_to_csv
from config import Config

def handle_user_input(prompt):
    return input(prompt)

def update_feature_file_with_user_input(feature_file_path, line_number_prompt, new_line_prompt):
    line_number = int(handle_user_input(line_number_prompt))
    new_line = handle_user_input(new_line_prompt)
    update_feature_file(feature_file_path, line_number, new_line)
    print("Feature file updated.")

def write_csv_file(feature_data, output_csv_path):
    write_to_csv(feature_data, output_csv_path)
    print(f"Successfully converted Gherkin file to CSV: {output_csv_path}")

def main():
    config = Config()

    feature_file_path = config.get_feature_file_path()
    output_csv_path = config.get_output_csv_path()

    create_backup(feature_file_path)
    feature_data = parse_feature_file(feature_file_path)

    while feature_data['errors']:
        print("Errors:")
        for error in feature_data['errors']:
            print(error)

        for error in feature_data['errors']:
            match = re.search(r'at line (\d+):', error)
            if match:
                line_number = int(match.group(1))
                line = error.split(': ')[-1]
                closest_match = find_closest_match(line, feature_data['valid_keywords'])
                if closest_match:
                    user_input = handle_user_input(f"Did you mean '{closest_match}' instead of '{line}'? (yes/no): ")
                    if user_input.lower() == 'yes':
                        update_feature_file(feature_file_path, line_number, closest_match)
                        feature_data = parse_feature_file(feature_file_path)
        else:
            break

    if feature_data['warnings']:
        print("Warnings:")
        for warning in feature_data['warnings']:
            print(warning)

    if not feature_data['errors']:
        print("The feature file is clean.")

    user_input = handle_user_input("Do you want to update the feature file? (yes/no): ")
    if user_input.lower() == 'yes':
        update_feature_file_with_user_input(feature_file_path, "Enter the line number to update: ", "Enter the new line content: ")

    user_input = handle_user_input("Do you want to undo the changes? (yes/no): ")
    if user_input.lower() == 'yes':
        restore_backup(feature_file_path)
        print("Changes have been undone.")

    user_input = handle_user_input("Do you want to continue and write the CSV file? (yes/no): ")
    if user_input.lower() == 'yes':
        write_csv_file(feature_data['features'], output_csv_path)
    else:
        print("Operation cancelled by the user.")
        sys.exit(0)
