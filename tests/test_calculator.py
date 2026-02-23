import pytest
from calculator import Calculator


class TestAdd:
    
    def test_positive(self):
        calc = Calculator()
        assert calc.add(5, 3) == 8
    
    def test_negative(self):
        calc = Calculator()
        assert calc.add(-5, -3) == -8
    
    def test_decimal(self):
        calc = Calculator()
        assert calc.add(2.5, 1.5) == pytest.approx(4.0)


class TestSubtract:
    
    def test_positive(self):
        calc = Calculator()
        assert calc.subtract(10, 4) == 6
    
    def test_negative_result(self):
        calc = Calculator()
        assert calc.subtract(4, 10) == -6
    
    def test_from_zero(self):
        calc = Calculator()
        assert calc.subtract(0, 5) == -5


class TestMultiply:
    
    def test_positive(self):
        calc = Calculator()
        assert calc.multiply(6, 7) == 42
    
    def test_by_zero(self):
        calc = Calculator()
        assert calc.multiply(5, 0) == 0
    
    def test_negative(self):
        calc = Calculator()
        assert calc.multiply(-3, -4) == 12


class TestDivide:
    
    def test_positive(self):
        calc = Calculator()
        assert calc.divide(20, 4) == pytest.approx(5.0)
    
    def test_decimal_result(self):
        calc = Calculator()
        assert calc.divide(10, 3) == pytest.approx(3.333333, rel=0.001)
    
    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(5, 0)
    
    def test_zero_divided(self):
        calc = Calculator()
        assert calc.divide(0, 5) == pytest.approx(0.0)


class TestEdgeCases:
    
    def test_large_numbers(self):
        calc = Calculator()
        assert calc.multiply(1000000, 1000000) == 1000000000000
    
    def test_clear(self):
        calc = Calculator()
        calc.result = 42
        result = calc.clear()
        assert result == 0
    
    def test_multiple_ops(self):
        calc = Calculator()
        r1 = calc.add(5, 3)
        r2 = calc.multiply(r1, 2)
        r3 = calc.subtract(r2, 4)
        assert r3 == 12
