import pytest
import sys

sys.path.append(r'D:\coding\functional_test')

from exercice1 import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    result = calculator.add(2, 3)
    assert result == 5
    assert calculator.get_memory() == 5

def test_subtract(calculator):
    result = calculator.subtract(5, 2)
    assert result == 3
    assert calculator.get_memory() == 3

def test_multiply(calculator):
    result = calculator.multiply(4, 3)
    assert result == 12
    assert calculator.get_memory() == 12

def test_divide(calculator):
    result = calculator.divide(10, 2)
    assert result == 5
    assert calculator.get_memory() == 5

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
    assert calculator.get_memory() == 0

def test_power(calculator):
    result = calculator.power(2, 3)
    assert result == 8
    assert calculator.get_memory() == 8

def test_sqrt(calculator):
    result = calculator.sqrt(16)
    assert result == 4
    assert calculator.get_memory() == 4

def test_sqrt_negative_number(calculator):
    with pytest.raises(ValueError):
        calculator.sqrt(-16)
    assert calculator.get_memory() == 0

def test_clear_memory(calculator):
    calculator.add(2, 3)
    calculator.clear_memory()
    assert calculator.get_memory() == 0
