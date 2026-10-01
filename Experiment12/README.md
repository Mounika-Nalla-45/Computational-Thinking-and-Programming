# 12. AI-Assisted Code Review, Refactoring and Testing

## Aim

To perform **AI-assisted code review, refactoring, and testing** of a Python program, and document where AI helped successfully and where manual intervention was required.

## Simple Algorithm

1. Write a simple Python program.
2. Use AI to review the code.
3. Identify errors and code improvements.
4. Refactor the code.
5. Write simple test cases.
6. Run the tests.
7. Compare the original and refactored code.
8. Record AI success and manual changes.

---

## Simple Program

### Original Program

```python
def calculate(a, b):
    result = a + b
    print("Result:", result)

calculate(10, 5)
```

### AI-Refactored Program

```python
def add_numbers(a: int, b: int) -> int:
    return a + b


def main():
    result = add_numbers(10, 5)
    print("Result:", result)


if __name__ == "__main__":
    main()
```

### Simple Test Program

```python
from app import add_numbers


def test_add_numbers():
    assert add_numbers(10, 5) == 15


def test_add_zero():
    assert add_numbers(10, 0) == 10
```

---

## Simple Data

```text
a = 10
b = 5
```

### Expected Output

```text
Result: 15
```

### Test Output

```text
============================= test session starts =============================
test_app.py::test_add_numbers PASSED
test_app.py::test_add_zero PASSED

============================== 2 passed ==============================
```

Run the test using:

```bash
pytest -v
```

---

## AI Review Findings

AI suggested:

- Add meaningful function name.
- Add type hints.
- Separate the main code from the function.
- Add automated tests.
- Use `if __name__ == "__main__":`.

### Where AI Succeeded

- Found code structure improvements.
- Suggested type hints.
- Created useful test cases.
- Improved readability.

### Where Manual Intervention Was Required

- Checked whether the refactored code gives the correct output.
- Verified the generated test cases.
- Decided which AI suggestions should be used.
- Ran the program and tests manually.

---

## Inference

- AI helped improve the code quickly.
- Refactored code is easier to read.
- Tests help verify correctness.
- Human checking is still required.

## Analysis

| Activity            | Result                     |
| ------------------- | -------------------------- |
| Code Review         | AI identified improvements |
| Refactoring         | Code became cleaner        |
| Testing             | Tests passed               |
| AI Contribution     | High for suggestions       |
| Manual Intervention | Required for verification  |

### Result

The Python program was successfully **reviewed, refactored, and tested with AI assistance**. AI provided useful improvements, while manual verification was required to confirm correctness.
