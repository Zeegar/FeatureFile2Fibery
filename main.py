import sys
import os
from csv_writer import write_to_csv
from config import Config

def main():
    config = Config()

    feature_file_path = config.get_feature_file_path()
    output_csv_path = config.get_output_csv_path()

    # Assuming feature_data is already validated and passed from inspectFeature.py
    feature_data = []  # Placeholder for the actual feature data

    write_to_csv(feature_data, output_csv_path)

    print(f"Successfully converted Gherkin file to CSV: {output_csv_path}")

if __name__ == "__main__":
    main()
