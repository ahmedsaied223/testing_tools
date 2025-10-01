import pytest
from src.calculator import Calculator


class TestCalculator:
"""Test cases for Calculator class"""

@pytest.fixture
def calc(self):
"""Create calculator instance"""
return Calculator()

# Parameterized tests for addition
@pytest.mark.parametrize("a,b,expected", [
(1, 2, 3),
(0, 0, 0),
(-1, 1, 0),
(2.5, 3.5, 6.0),
])
def test_add(self, calc, a, b, expected):
"""Test addition operation"""
result = calc.add(a, b)
assert result == expected

def test_subtract(self, calc):
"""Test subtraction operation"""
result = calc.subtract(5, 3)
assert result == 2

def test_multiply(self, calc):
"""Test multiplication operation"""
result = calc.multiply(3, 4)
assert result == 12

def test_divide(self, calc):
"""Test division operation"""
result = calc.divide(10, 2)
assert result == 5

def test_divide_by_zero(self, calc):
"""Test division by zero raises error"""
with pytest.raises(ValueError, match="Cannot divide by zero"):
calc.divide(10, 0)

@pytest.mark.parametrize("base,exponent,expected", [
(2, 3, 8),
(5, 0, 1),
(10, 1, 10),
])
def test_power(self, calc, base, exponent, expected):
"""Test power operation"""
result = calc.power(base, exponent)
assert result == expected

@pytest.mark.slow
def test_complex_calculation(self, calc):
"""Test complex calculation (marked as slow)"""
result = calc.add(calc.multiply(2, 3), calc.divide(10, 2))
assert result ==  11
