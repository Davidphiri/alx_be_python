import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test addition
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Regular addition
        self.assertEqual(self.calc.add(-1, 1), 0)  # Adding negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)  # Adding zeros
        self.assertEqual(self.calc.add(-5, -5), -10)  # Adding two negative numbers

    # Test subtraction
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Regular subtraction
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # Subtracting positive from negative
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Subtracting zeros
        self.assertEqual(self.calc.subtract(-5, -5), 0)  # Subtracting two equal negative numbers

    # Test multiplication
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Regular multiplication
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Multiplying negative and positive
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(-3, -3), 9)  # Multiplying two negatives

    # Test division
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 2), 3)  # Regular division
        self.assertEqual(self.calc.divide(-6, 2), -3)  # Dividing negative by positive
        self.assertEqual(self.calc.divide(5, 2), 2.5)  # Division with non-integer result
        self.assertEqual(self.calc.divide(0, 5), 0)  # Dividing zero by a number

        # Test division by zero (edge case)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero should return None
        self.assertIsNone(self.calc.divide(-5, 0))  # Division by zero with negative numerator
        self.assertIsNone(self.calc.divide(0, 0))  # Division by zero with zero numerator

if __name__ == "__main__":
    # Run the tests
    unittest.main()
