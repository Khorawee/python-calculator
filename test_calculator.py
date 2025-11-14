import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # ----- add() -----
    def test_add_basic(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-3, 10), 7)

    # ----- subtract() -----
    def test_subtract_basic(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1, 4), -5)

    # ----- multiply() -----
    def test_multiply_basic(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(0, 10), 0)

    # ----- divide() -----
    def test_divide_basic(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_remainder(self):
        self.assertEqual(self.calc.divide(7, 2), 3)

    # ----- modulo() -----
    def test_modulo_basic(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_equal(self):
        self.assertEqual(self.calc.modulo(7, 7), 0)

if __name__ == '__main__':
    unittest.main()
