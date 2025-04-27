from src.main import *

class TestCalculator:
    def test_add(self):
        assert add(3, 4) ==  7

    def test_subtract(self):
        assert subtract(10, 5) == 5

    def test_multiply(self):
        assert multiply(2, 3) == 6

    def test_divide(self):
        assert divide(10, 2) == 5

    def test_power(self):
        assert power(2, 3) == 8

