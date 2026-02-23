# Quick-Calc

A simple, yet comprehensive calculator application demonstrating professional software engineering practices including clean code, comprehensive testing, and version control.

## Project Description

Quick-Calc is a command-line calculator application that performs basic arithmetic operations. It showcases best practices in software development, including a multi-layered testing strategy (unit and integration tests), clean code architecture, and professional documentation. The project is designed to be easily extensible and maintainable, with a clear separation of concerns between the calculation logic and the user interface layer.

## Features

- **Addition**: Correctly adds two numbers (e.g., 5 + 3 = 8)
- **Subtraction**: Correctly subtracts two numbers (e.g., 10 − 4 = 6)
- **Multiplication**: Correctly multiplies two numbers (e.g., 6 × 7 = 42)
- **Division**: Correctly divides two numbers with graceful handling of division by zero
- **Clear (C)**: Resets the current input and result to zero
- **Decimal Support**: Handles decimal numbers in all operations
- **Error Handling**: Gracefully handles edge cases such as division by zero

## Project Structure

```
swe-testing-assignment/
├── calculator.py          # Core calculator logic
├── app.py                 # Command-line application interface
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py # Unit tests (10+ tests)
│   └── test_integration.py # Integration tests (6+ tests)
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── TESTING.md             # Detailed testing documentation
└── .gitignore             # Git ignore rules
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/swe-testing-assignment.git
cd swe-testing-assignment
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run the Application

To run the calculator from the command line:

```bash
python app.py
```

### Example Usage

```python
from app import CalculatorApp

# Create an instance
app = CalculatorApp()

# Input number 5
app.input_number(5)

# Perform addition
app.perform_operation("+")

# Input number 3
app.input_number(3)

# Calculate result
result = app.calculate()
print(f"Result: {result}")  # Output: Result: 8.0
```

## How to Run Tests

### Run All Tests
```bash
pytest
```

### Run Unit Tests Only
```bash
pytest tests/test_calculator.py -v
```

### Run Integration Tests Only
```bash
pytest tests/test_integration.py -v
```

### Run Tests with Coverage Report
```bash
pytest --cov=. --cov-report=html
```

### Run Tests in Verbose Mode
```bash
pytest -v
```

## Testing Framework Research: Pytest vs Unittest

### Overview
Both pytest and unittest are popular testing frameworks for Python. This project uses **pytest** as the primary testing framework. Below is a comparative analysis of both frameworks.

### Pytest Advantages
1. **Simple Syntax**: Pytest uses plain `assert` statements instead of specialized assertion methods, making tests more readable and intuitive. Example: `assert result == 8` vs `self.assertEqual(result, 8)`.

2. **Fixture System**: Pytest's fixture mechanism is more powerful and flexible than unittest's setUp/tearDown methods. Fixtures are reusable, composable, and can be shared across test files.

3. **Less Boilerplate**: Tests don't require class inheritance or setup/teardown methods, resulting in cleaner, more concise code.

4. **Better Output**: Pytest provides more detailed and readable output when tests fail, with better formatting of assertions.

5. **Parametrization**: Pytest's `@pytest.mark.parametrize` decorator makes it easy to run the same test with different inputs, reducing code duplication.

6. **Plugin Ecosystem**: Pytest has a rich ecosystem of plugins for extensions, coverage reporting, and CI/CD integration.

### Unittest Advantages
1. **Standard Library**: Unittest is part of the Python standard library, requiring no external dependencies.

2. **Familiar to Java/C# Developers**: The xUnit-style structure (TestCase classes, setUp/tearDown) is familiar to developers coming from Java or C#.

3. **Built-in Discovery**: Unittest has built-in test discovery mechanisms.

### Pytest Advantages Over Unittest
- **Test Discovery**: Both support test discovery, but pytest's is more automatic and requires less configuration.
- **Assertion Introspection**: Pytest provides detailed assertion introspection, showing exactly which part of the assertion failed.
- **Concurrency**: Pytest plugins like `pytest-xdist` make it easier to run tests in parallel.

### Why We Chose Pytest

For this project, **pytest** was selected for the following reasons:

1. **Code Quality**: The simpler syntax and less boilerplate lead to cleaner, more readable test code that is easier to maintain.

2. **Developer Experience**: Pytest's informative error messages and detailed output make debugging test failures faster and more intuitive.

3. **Scalability**: As the test suite grows, pytest's fixture system and parametrization features scale much better than unittest.

4. **Industry Standard**: Pytest is widely used in modern Python projects and is considered the de facto standard for testing in the Python community.

5. **Integration**: Pytest integrates seamlessly with popular tools like Jenkins, GitHub Actions, and other CI/CD platforms used in professional settings.

## Test Results

All tests pass successfully. Run `pytest -v` to see detailed test results.

## Contributing

This project is maintained as part of an educational assignment. Pull requests are welcome for improvements and bug fixes.

## License

This project is created for educational purposes as part of the Advanced Software Engineering course.

## Author

Student Developer
Email: student@example.com

---

**Last Updated**: February 2026
**Version**: 1.0.0
