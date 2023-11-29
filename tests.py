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