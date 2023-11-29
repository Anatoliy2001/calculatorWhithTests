import unittest
from calcul import MathOperation, Calculator
'''
Интеграционные тесты проверяют взаимодействие между классами или модулями.
В данном случае интеграционные тесты для класса Calculator проверяют его взаимодействие с классом MathOperation,
удостоверяясь, что методы Calculator, использующие методы MathOperation, возвращают ожидаемые результаты.
'''
class TestCalculatorIntegration(unittest.TestCase):
    def test_perform_square(self):
        math_op = MathOperation()
        calc = Calculator(math_op)
        self.assertEqual(calc.perform_square(4), 16)

    def test_perform_cube(self):
        math_op = MathOperation()
        calc = Calculator(math_op)
        self.assertEqual(calc.perform_cube(3), 27)

    def test_perform_factorial(self):
        math_op = MathOperation()
        calc = Calculator(math_op)
        self.assertEqual(calc.perform_factorial(5), 120)

if __name__ == '__main__':
    unittest.main()
