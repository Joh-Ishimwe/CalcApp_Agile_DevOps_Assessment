import pytest
from calculator import (
    add,
    subtract,
    multiply
)


# ─────────────────────────────
# SPRINT 1 TESTS
# ─────────────────────────────

class TestAddition:
    def test_add_two_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_with_zero(self):
        assert add(0, 5) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_decimals(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtraction:
    def test_subtract_two_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_gives_negative(self):
        assert subtract(3, 5) == -2

    def test_subtract_with_zero(self):
        assert subtract(5, 0) == 5

    def test_subtract_decimals(self):
        assert subtract(5.5, 2.5) == 3.0


class TestMultiplication:
    def test_multiply_two_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-3, 4) == -12

    def test_multiply_decimals(self):
        assert multiply(2.5, 4) == 10.0
