import json
import sys

def check_coverage(threshold):
    bright_red = '\033[91m'
    bright_green = '\033[92m'
    bright_yellow = '\033[93m'
    reset = '\033[0m'

    try:
        with open('coverage.json') as f:
            data = json.load(f)
        
        coverage = data['totals']['percent_covered']

        if coverage is None:
            print(f"{bright_red}No coverage information found.{reset}")
            sys.exit(1)

        print(f"Coverage: {coverage}%")

        if coverage < threshold:
            print(f"{bright_red}Coverage is below threshold. Expected at least {threshold}%, but got {coverage}%.{reset}")
            sys.exit(1)
        else:
            print(f"{bright_green}Coverage meets the threshold: {coverage}% >= {threshold}%{reset}")

    except json.JSONDecodeError:
        print(f"{bright_red}Failed to parse coverage JSON report.{reset}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"{bright_red}Coverage JSON report not found.{reset}")
        sys.exit(1)

if __name__ == "__main__":
    threshold = 99  # Adjust this threshold as needed
    check_coverage(threshold)
