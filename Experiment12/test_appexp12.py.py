from app import add_numbers


def test_add_numbers():
    assert add_numbers(10, 5) == 15


def test_add_zero():
    assert add_numbers(10, 0) == 10