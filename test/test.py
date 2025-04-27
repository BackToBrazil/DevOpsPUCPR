from src.main import *

class TestCalculator:
    def test_add():
        assert add(3, 4) ==  7

    def test_subtract():
        assert subtract(10, 5) == 5

    def test_multiply():
        assert multiply(2, 3) == 6

    def test_divide():
        assert divide(10, 2) == 5

    def test_power():
        assert power(2, 3) == 8

