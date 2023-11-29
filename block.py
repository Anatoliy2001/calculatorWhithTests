import unittest
from calcul import MathOperation, Calculator
'''
Блочные тесты используются для проверки отдельных блоков кода, таких как методы классов, 
на корректность их работы. В приведенных тестах для класса MathOperation тестируются его методы:
_square, _cube и _factorial, а для класса Calculator - методы:
 add, subtract и multiply.
 Они обеспечивают проверку того, что каждый метод работает корректно в изоляции.
'''
class TestMathOperation(unittest.TestCase):
    def test_square(self):
        math_op = MathOperation()
        self.assertEqual(math_op._square(5), 25)

    def test_cube(self):
        math_op = MathOperation()
        self.assertEqual(math_op._cube(4), 64)

    def test_factorial(self):
        math_op = MathOperation()
        self.assertEqual(math_op._factorial(5), 120)

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator(MathOperation())
        self.assertEqual(calc.add(3, 7), 10)

    def test_subtract(self):
        calc = Calculator(MathOperation())
        self.assertEqual(calc.subtract(10, 7), 3)

    def test_multiply(self):
        calc = Calculator(MathOperation())
        self.assertEqual(calc.multiply(4, 6), 24)

if __name__ == '__main__':
    unittest.main()