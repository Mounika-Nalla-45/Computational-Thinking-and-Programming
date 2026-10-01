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