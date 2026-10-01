# 13. Specification-First, Type-Driven and Test-First Development with AI

## Aim

To implement a Python program using **specification-first, type-driven, and test-first development with AI assistance**.

## 1. Simple Algorithm

1. Write the program requirements first.
2. Define the function using proper data types.
3. Write test cases before writing the actual program.
4. Run the tests and observe the initial failure.
5. Write the Python program.
6. Run the tests again.
7. Use AI to review the specification, types, and tests.
8. Manually verify the final result.

---

# 2. Specification

**Requirement:** Create a function to calculate the total price.

```text
Input:
price = price of one item
quantity = number of items

Rules:
price must be 0 or more
quantity must be 0 or more

Output:
total = price × quantity
```

### Function specification

```python
calculate_total(price: float, quantity: int) -> float
```

This is the **type-driven** part because the input and output types are clearly defined.

---

# 3. How to Do It in VS Code

Create a folder:

```text
F:\CTP\MyProject\Experiment13
```

Inside it create:

```text
Experiment13
│
├── test_total.py
└── total.py
```

---

## Step 1: Open the folder in VS Code

Open:

```text
F:\CTP\MyProject\SpecificationProject
```

Then open:

**Terminal → New Terminal**

---

## Step 2: Install pytest

Run:

```powershell
py -m pip install pytest
```

---

# 4. Test-First Development

Create **`test_total.py` first**.

```python
from total import calculate_total


def test_normal():
    assert calculate_total(100.0, 3) == 300.0


def test_zero_quantity():
    assert calculate_total(100.0, 0) == 0.0


def test_zero_price():
    assert calculate_total(0.0, 5) == 0.0
```

Save with:

```text
Ctrl + S
```

---

## Step 3: Run the Test Before Writing the Program

Run:

```powershell
py -m pytest -v
```

Initially, the test will fail because `total.py` does not exist.

You may see:

```text
ERROR
ModuleNotFoundError: No module named 'total'
```

This shows **test-first development**: the tests were created before the actual program.

---

# 5. Write the Python Program

Now create **`total.py`**:

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity


if __name__ == "__main__":
    price = 100.0
    quantity = 3

    total = calculate_total(price, quantity)

    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)
```

Save:

```text
Ctrl + S
```

---

# 6. Run the Program

In VS Code terminal:

```powershell
py total.py
```

### Output

```text
Price: 100.0
Quantity: 3
Total: 300.0
```

---

# 7. Run the Tests Again

```powershell
py -m pytest -v
```

### Output

```text
test_total.py::test_normal PASSED
test_total.py::test_zero_quantity PASSED
test_total.py::test_zero_price PASSED

3 passed
```

---

# 8. Using AI

You can use AI in VS Code or ChatGPT to support each stage.

### Prompt for specification

```text
Create a simple specification for a Python function
that calculates total price from price and quantity.
Include input, output, and rules.
```

### Prompt for type-driven design

```text
Give the Python function signature for the above specification
using suitable type hints.
```

Expected:

```python
calculate_total(price: float, quantity: int) -> float
```

### Prompt for test-first development

```text
Create pytest test cases for the specification.
Write the tests without writing the implementation.
```

AI can generate:

```python
def test_normal():
    assert calculate_total(100.0, 3) == 300.0
```

Then you manually create the implementation and run the tests.

---

# 9. Simple Data

```text
Price = 100.0
Quantity = 3
```

### Calculation

```text
100.0 × 3 = 300.0
```

---

# 10. Result

```text
Price: 100.0
Quantity: 3
Total: 300.0

3 passed
```

The program and all test cases executed successfully.

---

# 11. Inference

- Specification defines what the program should do.
- Type hints define the expected data types.
- Tests are written before the implementation.
- AI helps create specifications, types, and tests.
- Manual checking confirms the final program.

# 12. Analysis

| Method              | Purpose                        |
| ------------------- | ------------------------------ |
| Specification-first | Defines requirements first     |
| Type-driven         | Uses clear type hints          |
| Test-first          | Tests are written before code  |
| AI assistance       | Helps generate and review code |
| Manual verification | Checks the final result        |

### Final Result

The program was successfully developed using **specification-first, type-driven, and test-first development with AI assistance**, and the final implementation passed all tests.
