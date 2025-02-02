import sys
from gherkin_parser import parse_feature_file, find_closest_match, update_feature_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python inspectFeature.py <feature_file_path>")
        sys.exit(1)

    feature_file_path = sys.argv[1]
    feature_data = parse_feature_file(feature_file_path)

    while feature_data['errors']:
        print("Errors:")
        for error in feature_data['errors']:
            print(error)

        for error in feature_data['errors']:
            line_number = int(error.split(' ')[-1].strip(':'))
            line = error.split(': ')[-1]
            closest_match = find_closest_match(line, feature_data['valid_keywords'])
            if closest_match:
                user_input = input(f"Did you mean '{closest_match}' instead of '{line}'? (yes/no): ")
                if user_input.lower() == 'yes':
                    update_feature_file(feature_file_path, line_number, closest_match)
                    feature_data = parse_feature_file(feature_file_path)
                    break
        else:
            break

    if feature_data['warnings']:
        print("Warnings:")
        for warning in feature_data['warnings']:
            print(warning)

    if not feature_data['errors']:
        print("The feature file is clean.")

if __name__ == "__main__":
    main()
