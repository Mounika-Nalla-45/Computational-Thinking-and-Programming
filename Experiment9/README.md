# 9. Unit and Integration Testing

## Question

Write comprehensive unit and integration tests for a Python application using `pytest` and `Hypothesis`.

### Aim

To test a Python application using unit testing, integration testing, `pytest`, and `Hypothesis`.

### Algorithm

1. Create a simple calculator application.
2. Test individual functions using `pytest`.
3. Generate different inputs using `Hypothesis`.
4. Test multiple functions together.
5. Run all tests.
6. Display the test results.

### Program

#### `calculator.py`

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calculate(a, b):
    return add(a, b), multiply(a, b)
```

#### `test_calculator.py`

```python
from calculator import add, multiply, calculate
from hypothesis import given, strategies as st


# Unit test
def test_add():
    assert add(2, 3) == 5


# Unit test
def test_multiply():
    assert multiply(2, 3) == 6


# Hypothesis test
@given(st.integers(), st.integers())
def test_add_hypothesis(a, b):
    assert add(a, b) == a + b


# Integration test
def test_calculate():
    result = calculate(4, 5)
    assert result == (9, 20)
```

### Input

```text
a = 4
b = 5
```

Hypothesis automatically generates additional integer values.

### Command

```bash
pip install pytest hypothesis
pytest test_calculator.py -v
```

### Output

```text
============================= test session starts =============================

test_calculator.py::test_add PASSED
test_calculator.py::test_multiply PASSED
test_calculator.py::test_add_hypothesis PASSED
test_calculator.py::test_calculate PASSED

============================== 4 passed in 1.25s ==============================
```

### Inference

* `pytest` checks the functions.
* `Hypothesis` generates different inputs automatically.
* Unit testing checks individual functions.
* Integration testing checks functions working together.

### Analysis

* **Pytest:** Runs and reports tests.
* **Hypothesis:** Generates test data automatically.
* **Unit Test:** Tests one function.
* **Integration Test:** Tests multiple functions together.

### Result

The Python application was successfully tested using `pytest` and `Hypothesis`, including unit and integration tests.
