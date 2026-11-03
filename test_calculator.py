import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    """Fixture providing a fresh Calculator instance for tests."""
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(3, 5) == -2
    assert calc.subtract(0, 0) == 0

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(5, 0) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(7, 2) == 3.5
    
    # Test division by zero raises ValueError
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        calc.divide(5, 0)
