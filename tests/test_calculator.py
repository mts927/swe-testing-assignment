"""
Unit tests for the Calculator class.
Tests individual calculator methods in isolation.
"""

import pytest
from calculator import Calculator


class TestCalculatorAddition:
    """Unit tests for addition operation."""

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers (5 + 3 = 8)."""
        calc = Calculator()
        result = calc.add(5, 3)
        assert result == 8

    def test_add_negative_numbers(self):
        """Test addition with negative numbers (-5 + -3 = -8)."""
        calc = Calculator()
        result = calc.add(-5, -3)
        assert result == -8

    def test_add_decimal_numbers(self):
        """Test addition with decimal numbers (2.5 + 1.5 = 4.0)."""
        calc = Calculator()
        result = calc.add(2.5, 1.5)
        assert result == pytest.approx(4.0)


class TestCalculatorSubtraction:
    """Unit tests for subtraction operation."""

    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers (10 - 4 = 6)."""
        calc = Calculator()
        result = calc.subtract(10, 4)
        assert result == 6

    def test_subtract_with_negative_result(self):
        """Test subtraction resulting in negative number (4 - 10 = -6)."""
        calc = Calculator()
        result = calc.subtract(4, 10)
        assert result == -6

    def test_subtract_from_zero(self):
        """Test subtraction from zero (0 - 5 = -5)."""
        calc = Calculator()
        result = calc.subtract(0, 5)
        assert result == -5


class TestCalculatorMultiplication:
    """Unit tests for multiplication operation."""

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers (6 * 7 = 42)."""
        calc = Calculator()
        result = calc.multiply(6, 7)
        assert result == 42

    def test_multiply_by_zero(self):
        """Test multiplication by zero (5 * 0 = 0)."""
        calc = Calculator()
        result = calc.multiply(5, 0)
        assert result == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication of negative numbers (-3 * -4 = 12)."""
        calc = Calculator()
        result = calc.multiply(-3, -4)
        assert result == 12


class TestCalculatorDivision:
    """Unit tests for division operation."""

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers (20 / 4 = 5)."""
        calc = Calculator()
        result = calc.divide(20, 4)
        assert result == pytest.approx(5.0)

    def test_divide_resulting_in_decimal(self):
        """Test division resulting in decimal (10 / 3 ≈ 3.33)."""
        calc = Calculator()
        result = calc.divide(10, 3)
        assert result == pytest.approx(3.333333, rel=0.001)

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError (5 / 0)."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(5, 0)

    def test_divide_zero_by_number(self):
        """Test division of zero by non-zero number (0 / 5 = 0)."""
        calc = Calculator()
        result = calc.divide(0, 5)
        assert result == pytest.approx(0.0)


class TestCalculatorEdgeCases:
    """Unit tests for edge cases and special scenarios."""

    def test_very_large_numbers(self):
        """Test calculation with very large numbers."""
        calc = Calculator()
        result = calc.multiply(1000000, 1000000)
        assert result == 1000000000000

    def test_clear_resets_to_zero(self):
        """Test that clear operation resets result to zero."""
        calc = Calculator()
        calc.result = 42
        result = calc.clear()
        assert result == 0
        assert calc.result == 0

    def test_consecutive_operations(self):
        """Test multiple consecutive operations."""
        calc = Calculator()
        result1 = calc.add(5, 3)  # 8
        result2 = calc.multiply(result1, 2)  # 16
        result3 = calc.subtract(result2, 4)  # 12
        assert result3 == 12
