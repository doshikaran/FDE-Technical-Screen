# FDE Technical Screen: Package Sorting Function

## Overview
This project implements a function, `main`, to categorize packages into different stacks based on their dimensions and weight. The function is designed to assist Thoughtful’s robotic automation factory in dispatching packages effectively.

The rules for sorting are as follows:

### A package is **bulky** if:
- Its volume (Width × Height × Length) is greater than or equal to 1,000,000 cm³.
- **OR** any of its dimensions is greater than or equal to 150 cm.

### A package is **heavy** if:
- Its mass is greater than or equal to 20 kg.

## Stacks
Packages are sorted into the following stacks:
1. **STANDARD**: Packages that are neither bulky nor heavy.
2. **SPECIAL**: Packages that are either bulky or heavy but not both.
3. **REJECTED**: Packages that are both bulky and heavy.

---

## Getting Started
Prerequisites
Python 3.x installed on your system.
Files
main.py: Contains the main function and example test cases.
test_main.py: Automated test suite for the main function.

## Running the Code
**Run the Sorting Function**
Execute the main.py script to test the function with predefined examples:
_python3 main.py_

**Example Output**
STANDARD
SPECIAL
SPECIAL
REJECTED
STANDARD
REJECTED

---

## Testing
The project includes an automated test suite to validate the function. Tests are written using Python’s unittest framework. Run the tests as follows:
_python3 -m unittest test_main.py_

Sample Output
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK

---

## Test Coverage
The test suite ensures:

Coverage of all logic branches (neither, either, and both).
Validation of edge cases at and just below the thresholds for bulkiness and heaviness.

## Key Features
Accurate Classification: Ensures packages are sorted correctly based on provided rules.
Edge Case Handling: Covers tricky scenarios like threshold conditions.
Test Automation: Includes a robust test suite for quick validation.


