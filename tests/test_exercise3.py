import pytest
import sys
from math import pi

sys.path.append(r'D:\coding\functional_test')

from exercice3 import *

@pytest.fixture
def rectangle():
    return Rectangle(4, 5)

@pytest.fixture
def circle():
    return Circle(3)

@pytest.fixture
def square():
    return Square(4)

def test_rectangle_area(rectangle):
    result = rectangle.area()
    assert result == 20

def test_rectangle_perimeter(rectangle):
    result = rectangle.perimeter()
    assert result == 18

def test_circle_area(circle):
    result = circle.area()
    assert result == pytest.approx(28.274, rel=1e-3)

def test_circle_perimeter(circle):
    result = circle.perimeter()
    assert result == pytest.approx(18.85, rel=1e-3)

def test_square_area(square):
    result = square.area()
    assert result == 16

def test_square_perimeter(square):
    result = square.perimeter()
    assert result == 16


