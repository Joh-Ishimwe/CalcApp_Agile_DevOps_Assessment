import pytest
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    save_to_history,
    get_history,
    history
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


# ─────────────────────────────
# SPRINT 2 TESTS
# ─────────────────────────────

class TestDivision:
    def test_divide_two_positive_numbers(self):
        assert divide(10, 2) == 5

    def test_divide_gives_decimal(self):
        assert divide(7, 2) == 3.5

    def test_divide_negative_numbers(self):
        assert divide(-10, 2) == -5

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError) as error:
            divide(10, 0)
        assert "Cannot divide by zero" in str(error.value)

    def test_divide_by_zero_does_not_crash(self):
        try:
            divide(5, 0)
        except ValueError:
            pass  # expected, app should not crash


class TestHistory:
    def setup_method(self):
        # Clear history before each test
        history.clear()

    def test_history_starts_empty(self):
        assert get_history() == []

    def test_save_to_history(self):
        save_to_history("2 + 3 = 5")
        assert "2 + 3 = 5" in get_history()

    def test_history_saves_multiple_entries(self):
        save_to_history("2 + 3 = 5")
        save_to_history("10 / 2 = 5")
        assert len(get_history()) == 2

    def test_history_preserves_order(self):
        save_to_history("first")
        save_to_history("second")
        assert get_history()[0] == "first"
        assert get_history()[1] == "second"