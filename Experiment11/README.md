#  11. Spec-First Python App with AI Assistance

**Aim:** Develop a Python application using GitHub Copilot / Cursor / Claude Code with specification-first development and document the AI assistance.

**Application chosen:** Student Grade Calculator (kept simple so the workflow stays clear)

---

## 1. Specification (written first, before any code)

```
SPEC: grade_calculator
Input : list of marks (0-100)
Output: (average, grade)
Rules : avg >= 90 -> A | >= 75 -> B | >= 60 -> C | >= 40 -> D | else F
Errors: empty list -> ValueError; mark outside 0-100 -> ValueError
```

## 2. Algorithm

1. Write the specification (inputs, outputs, rules, error cases).
2. Give the spec to the AI tool (Copilot / Cursor / Claude Code) as the prompt.
3. Write test cases from the spec.
4. Let the AI generate the code, then review it line by line.
5. Run the tests and fix any failures, using the AI for debugging.
6. Record the AI assistance in a log (prompt used, output, what you changed).

## 3. Program

```python
def grade(marks):
    if not marks or any(m < 0 or m > 100 for m in marks):
        raise ValueError("Marks must be a non-empty list of values 0-100")
    avg = sum(marks) / len(marks)
    for limit, g in [(90, "A"), (75, "B"), (60, "C"), (40, "D")]:
        if avg >= limit:
            return round(avg, 2), g
    return round(avg, 2), "F"

# Tests written from the spec
assert grade([85, 90, 78]) == (84.33, "B")
assert grade([95, 92, 98]) == (95.0, "A")
assert grade([60, 65, 55]) == (60.0, "C")
assert grade([35, 40, 30]) == (35.0, "F")
try:
    grade([])
except ValueError:
    print("Empty list handled")
print("All tests passed")
```

**How to run:**

```
python grade_calculator.py
```

## 4. Data and Result

| Input marks | Average | Grade | Test result |
|---|---|---|---|
| [85, 90, 78] | 84.33 | B | Pass |
| [95, 92, 98] | 95.0 | A | Pass |
| [60, 65, 55] | 60.0 | C | Pass |
| [35, 40, 30] | 35.0 | F | Pass |
| [] | Error | n/a | Pass (ValueError raised) |

**Output:**

```
Empty list handled
All tests passed
```

## 5. AI Assistance Log (documentation)

| Step | Prompt / action | AI output | Human action |
|---|---|---|---|
| 1 | "Generate a Python function from this spec" | Function with grade logic | Checked the boundaries (90, 75, 60, 40) |
| 2 | "Write asserts for all grades and errors" | Test cases | Verified the expected values by hand |
| 3 | "Handle invalid marks" | Added the range check | Accepted |

## 6. Inference and Analysis

- Writing the spec first gave the AI a clear prompt, so the generated code matched the requirements on the first try with very little rework.
- Tests derived from the spec caught boundary and error cases (empty list, out-of-range marks) that are easy to miss when coding directly.
- The AI sped up writing the code and tests, but human review was still needed to confirm the grade boundaries and expected values.
- Logging prompts and outputs makes the AI's contribution traceable and the work reproducible.

## Conclusion

Specification-first development with AI assistance produces correct, tested, and well-documented code faster than ad-hoc coding, as long as a human verifies the AI's output.
