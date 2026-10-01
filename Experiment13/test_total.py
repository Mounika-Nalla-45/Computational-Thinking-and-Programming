from total import calculate_total


def test_normal():
    assert calculate_total(100.0, 3) == 300.0


def test_zero_quantity():
    assert calculate_total(100.0, 0) == 0.0


def test_zero_price():
    assert calculate_total(0.0, 5) == 0.0