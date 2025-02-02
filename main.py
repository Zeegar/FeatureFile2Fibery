import sys
import os
from gherkin_parser import parse_feature_file
from csv_writer import write_to_csv
from config import Config

def main():
    config = Config()

    feature_file_path = config.get_feature_file_path()
    output_csv_path = config.get_output_csv_path()

    feature_data = parse_feature_file(feature_file_path)

    if feature_data['errors']:
        print("Errors:")
        for error in feature_data['errors']:
            print(error)

    if feature_data['warnings']:
        print("Warnings:")
        for warning in feature_data['warnings']:
            print(warning)

    write_to_csv(feature_data['features'], output_csv_path)

    print(f"Successfully converted Gherkin file to CSV: {output_csv_path}")

if __name__ == "__main__":
    main()
