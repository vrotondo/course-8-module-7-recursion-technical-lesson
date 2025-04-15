# Recursive Fibonacci in Python

## What You'll Learn

- Write a recursive function to compute Fibonacci numbers.
- Understand and define base cases in recursion.
- Trace recursion depth using print statements.
- Analyze performance and time complexity.
- Compare recursive vs. iterative behavior.

---

## Project Structure

```
.
├── fibonacci_demo.py
├── lib/
│   ├── __init__.py
│   └── fibonacci.py
├── test_fibonacci.py
├── Pipfile
├── Pipfile.lock
├── pytest.ini
└── README.md
```

---

## How to Start

1. Install dependencies:

**Using Pipenv:**
```bash
pipenv install
pipenv shell
```

---

## Your Task

- Implement `fibonacci(n)` to return the nth Fibonacci number using recursion.
- Identify and return results for the base cases: `n == 0` and `n == 1`.
- Recursively compute `fibonacci(n-1) + fibonacci(n-2)` for other values.
- Implement `fibonacci_debug(n, depth=0)` to print call stack depth.
- Use `fibonacci_demo.py` to manually test the function with debug output.
- Run `pytest` and pass all the tests in `test_fibonacci.py`.

---

## Running the Demo

Use the demo script to visualize recursion:

```bash
python fibonacci_demo.py
```

You’ll see the call structure and final return values for small Fibonacci numbers.

---

## Running Tests

Use pytest to validate your logic:

```bash
pytest
```

Tests will initially fail. Implement both functions in `fibonacci.py` to make them pass.

---

## Tips

- Start with base cases and test with `n = 0` and `n = 1`.
- Use `print()` inside the recursive function to visualize how calls expand and collapse.
- Be aware of performance: this version has exponential time complexity.

---
