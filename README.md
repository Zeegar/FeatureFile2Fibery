# FeatureFile2Fibery
A tool for extracting Test Cases, and Steps ready to be entered into Fibery 

## Overview

`inspectFeature.py` is a Python script that parses Gherkin feature files and converts their content into a CSV format. This tool extracts features, scenarios, and steps from Gherkin files and organises them into a structured CSV file ready to be uploaded to Fibery.

## Features

- Parses Gherkin feature files to extract features, scenarios, and steps.
- Handles `Feature:`, `Scenario:`, `Scenario Outline:`, and `Developer Task:` lines.
- Includes scenarios and developer tasks even if they don't have steps.
- Generates a CSV file with the extracted data.
- Checks the formatting of the feature file and reports any formatting errors.

## Usage

### Prerequisites

- Python 3.x

### Running the Script

1. Place your Gherkin feature file in the same directory as `inspectFeature.py` or provide the full path to the feature file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `inspectFeature.py`.
4. Run the script with the following command:

   ```sh
   python inspectFeature.py <feature_file_path>
   ```

5. After the script checks the formatting and parses the feature file, it will prompt you to confirm whether you want to continue and write the CSV file. Type `yes` to proceed or `no` to cancel the operation.

### Configuration Management

The script now uses a `Config` class to manage file paths and command-line arguments. This class is defined in the `config.py` file.

### Example

```python
from config import Config

config = Config()
feature_file_path = config.get_feature_file_path()
output_csv_path = config.get_output_csv_path()
```

### Running the Inspection Script

1. Place your Gherkin feature file in the same directory as `inspectFeature.py` or provide the full path to the feature file.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `inspectFeature.py`.
4. Run the script with the following command:

   ```sh
   python inspectFeature.py <feature_file_path>
   ```

5. The script will display a summary of any formatting errors or syntax issues found in the feature file. It will also handle non-numeric characters in error messages to avoid the ValueError.

### New Behavior of `inspectFeature.py`

The `inspectFeature.py` script has been updated to find lines close to the target Gherkin syntax and ask the user for confirmation. It updates the original file with the new changes and parses the file again. If there are no more errors, the script returns a message indicating the feature file is clean.

### State Management, Backup Creation, and Undo Functionality

The `inspectFeature.py` script now includes state management, creates a backup of the original file before modifications, and provides a way to undo changes. This ensures that the original file is preserved and changes can be reverted if needed.

## Additional Files

- `gherkin_parser.py`: Contains the function to parse Gherkin feature files.
- `csv_writer.py`: Contains the function to write parsed data to a CSV file.
- `format_checker.py`: Contains the function to check the formatting of the feature file.
- `config.py`: Contains the `Config` class to manage file paths and command-line arguments.
