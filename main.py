import sys
import os
from csv_writer import write_to_csv
from config import Config
from gherkin_parser import parse_feature_file

def main():
    config = Config()

    feature_file_path = config.get_feature_file_path()
    output_csv_path = config.get_output_csv_path()

    # Assuming feature_data is already validated and passed from inspectFeature.py
    feature_data = []  # Placeholder for the actual feature data

    feature_data = parse_feature_file(feature_file_path)
    feature_data = feature_data['features']

    user_input = input("Do you want to continue and write the CSV file? (yes/no): ")
    if user_input.lower() == 'yes':
        write_to_csv(feature_data, output_csv_path)
        print(f"Successfully converted Gherkin file to CSV: {output_csv_path}")
    else:
        print("Operation cancelled by the user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
