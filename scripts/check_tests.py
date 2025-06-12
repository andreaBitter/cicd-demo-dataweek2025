import os
import sys

ANALYSIS_DIR = "app/analysis"
TESTS_DIR = "tests"
EXPECTED_PREFIX = "test_"

# Get all analysis modules (excluding __init__.py)
analysis_files = [
    f for f in os.listdir(ANALYSIS_DIR)
    if f.endswith(".py") and f != "__init__.py"
]

# Check for corresponding test files
missing_tests = []
for fname in analysis_files:
    test_name = f"{EXPECTED_PREFIX}{fname}"
    if not os.path.exists(os.path.join(TESTS_DIR, test_name)):
        missing_tests.append(test_name)

# Fail if any test is missing
if missing_tests:
    print("Missing test files for analysis modules:")
    for missing in missing_tests:
        print(f" - {missing}")
    sys.exit(1)
else:
    print("All analysis modules have corresponding test files.")