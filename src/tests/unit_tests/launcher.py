import pytest
from check_coverage import check_coverage

params = [
        "--cov=src/tests/unit_tests/test_cases/", 
        "--cov-report=json:coverage.json",
    ]

# ▶️ generate the HTML report:
result = pytest.main(params)
threshold = 10  # Adjust this threshold as needed
check_coverage(threshold)