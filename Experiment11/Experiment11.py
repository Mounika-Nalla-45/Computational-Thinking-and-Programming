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