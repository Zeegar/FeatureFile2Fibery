import sys
from gherkin_parser import parse_feature_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python inspectFeature.py <feature_file_path>")
        sys.exit(1)

    feature_file_path = sys.argv[1]
    feature_data = parse_feature_file(feature_file_path)

    if feature_data['errors']:
        print("Errors:")
        for error in feature_data['errors']:
            print(error)

    if feature_data['warnings']:
        print("Warnings:")
        for warning in feature_data['warnings']:
            print(warning)

    if feature_data['errors']:
        decision = input("Would you like to continue with CSV generation despite these issues? (yes/no): ")
        if decision.lower() != 'yes':
            print("CSV generation aborted due to errors.")
            sys.exit(1)

    print("No critical issues found. You can proceed with CSV generation.")

if __name__ == "__main__":
    main()
