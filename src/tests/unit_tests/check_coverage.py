import json
import sys

def check_coverage(threshold):
    try:
        with open('coverage.json') as f:
            data = json.load(f)
        
        coverage = data['totals']['percent_covered']

        if coverage is None:
            print("No coverage information found.")
            sys.exit(1)

        print(f"Coverage: {coverage}%")

        if coverage < threshold:
            print(f"Coverage is below threshold. Expected at least {threshold}%, but got {coverage}%.")
            sys.exit(1)
        else:
            print(f"Coverage meets the threshold: {coverage}% >= {threshold}%")

    except json.JSONDecodeError:
        print("Failed to parse coverage JSON report.")
        sys.exit(1)
    except FileNotFoundError:
        print("Coverage JSON report not found.")
        sys.exit(1)

if __name__ == "__main__":
    threshold = 80  # Adjust this threshold as needed
    check_coverage(threshold)
