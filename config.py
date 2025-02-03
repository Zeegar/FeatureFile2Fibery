import os
import sys

class Config:
    def __init__(self):
        self.feature_file_path = self.parse_command_line_args()

    def parse_command_line_args(self):
        if len(sys.argv) != 2:
            print("Usage: python main.py <feature_file_path>")
            sys.exit(1)
        return sys.argv[1]

    def get_feature_file_path(self):
        return self.feature_file_path

    def get_output_csv_path(self):
        base_name = os.path.splitext(os.path.basename(self.feature_file_path))[0]
        output_csv_path = f"{base_name}.csv"

        counter = 1
        while os.path.exists(output_csv_path):
            output_csv_path = f"{base_name}_{counter}.csv"
            counter += 1

        return output_csv_path
