import sys
import os
from gherkin_parser import parse_feature_file_from_path
from csv_writer import write_to_csv_from_path
from format_checker import check_formatting_from_path

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <feature_file_path>")
        sys.exit(1)

    feature_file_path = sys.argv[1]
    base_name = os.path.splitext(os.path.basename(feature_file_path))[0]
    output_csv_path = f"{base_name}.csv"

    counter = 1
    while os.path.exists(output_csv_path):
        output_csv_path = f"{base_name}_{counter}.csv"
        counter += 1

    with open(feature_file_path, 'r') as feature_file:
        formatting_result = check_formatting_from_path(feature_file)
        if formatting_result != "Formatting Ok":
            print(formatting_result)

        feature_data = parse_feature_file_from_path(feature_file)
        with open(output_csv_path, 'w', newline='') as output_csv_file:
            write_to_csv_from_path(feature_data, output_csv_file)

    print(f"Successfully converted Gherkin file to CSV: {output_csv_path}")

if __name__ == "__main__":
    main()
