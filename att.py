import unittest
from calcul import MathOperation, Calculator
'''
Аттестационные тесты (или acceptance tests)проверяют соответствие программы спецификациям и требованиям.
В приведенных тестах проверяется, что калькулятор корректно выполняет все операции, отражая требования спецификаций программы.
Каждый тип тестов имеет свою функциональность и цель,
и их сочетание обеспечивает надежное покрытие тестами для проверки корректности работы программы в целом.
'''
class TestCalculatorAcceptance(unittest.TestCase):
    def test_calculator_operations(self):
        math_op = MathOperation()
        calc = Calculator(math_op)
        # Проверить, что калькулятор правильно выполняет все операции
        self.assertEqual(calc.add(3, 7), 10)
        self.assertEqual(calc.subtract(10, 7), 3)
        self.assertEqual(calc.multiply(4, 6), 24)
        self.assertEqual(calc.perform_square(4), 16)
        self.assertEqual(calc.perform_cube(3), 27)
        self.assertEqual(calc.perform_factorial(5), 120)

if __name__ == '__main__':
    unittest.main()
