from src.main import add
from src.main import subtract
from src.main import multiply
from src.main import divide
from src.main import power

class TestCalculator:
    def test_add(self, a, b):
        assert add() ==  a + b

    def test_subtract(self, a, b):
        assert subtract() == a - b

    def test_multiply(self, a, b):
        assert multiply() == a * b

    def test_divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        assert divide() == a / b

    def test_power(self, a, b):
        assert power() == a ** b
