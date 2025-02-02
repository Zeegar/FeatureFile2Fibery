import sys
import os
from gherkin_parser import parse_feature_file
from csv_writer import write_to_csv
from format_checker import check_formatting
from config import Config

def main():
    config = Config()

    feature_file_path = config.get_feature_file_path()
    output_csv_path = config.get_output_csv_path()

    formatting_result = check_formatting(feature_file_path)
    if formatting_result != "Formatting Ok":
        print(formatting_result)

    feature_data = parse_feature_file(feature_file_path)
    write_to_csv(feature_data, output_csv_path)

    print(f"Successfully converted Gherkin file to CSV: {output_csv_path}")

if __name__ == "__main__":
    main()
