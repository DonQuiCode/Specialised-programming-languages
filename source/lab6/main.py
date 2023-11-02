import unittest 
import sys 

from constants import home_path
sys.path.append(home_path + 'source/lab2')

from calculator import Calculator

from constants import home_path
sys.path.append(home_path + 'source/lab1')

from calculator_funcs import *


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculator.num1 = 5
        self.calculator.num2 = 3

    def test_addition(self):
        self.assertEqual(self.calculator.operations['+'](self.calculator.num1, self.calculator.num2), 8)
        self.assertEqual(self.calculator.operations['+'](self.calculator.num1, -self.calculator.num2), 2)

    def test_subtraction(self):
       self.assertEqual(self.calculator.operations['-'](self.calculator.num1, self.calculator.num2), 2)
       self.assertEqual(self.calculator.operations['-'](-self.calculator.num1, -self.calculator.num2), -2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.operations['*'](self.calculator.num1, self.calculator.num2), 15)
        self.assertEqual(self.calculator.operations['*'](self.calculator.num1, -self.calculator.num2), -15)
        self.assertEqual(self.calculator.operations['*'](self.calculator.num1, 0), 0)

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.operations['/'](self.calculator.num1, 0)
        self.assertAlmostEqual(self.calculator.operations['/'](self.calculator.num1, self.calculator.num2), 1.6666666666666667)
        self.assertEqual(self.calculator.operations['/'](10, -5), -2)

    def test_invalid_operator(self):
        self.calculator.operations = {'$': add}  # Invalid operator
        with self.assertRaises(KeyError):
            self.calculator.operations['+'](self.calculator.num1, self.calculator.num2)

if __name__ == '__main__':
    unittest.main()