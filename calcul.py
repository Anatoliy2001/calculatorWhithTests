class MathOperation:
    def __init__(self):
        pass
    
    def _square(self, num):
        # Метод для вычисления квадрата числа
        return num * num
    
    def _cube(self, num):
        # Метод для вычисления куба числа
        return num ** 3

    def _factorial(self, num):
        # Метод для вычисления факториала числа
        if num == 0 or num == 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
class Calculator:
    def __init__(self, math_operation):
        # Конструктор класса Calculator
        self.math_operation = math_operation
    
    def add(self, num1, num2):
        # Метод для выполнения сложения
        return num1 + num2

    def subtract(self, num1, num2):
        # Метод для выполнения вычитания
        return num1 - num2
    
    def multiply(self, num1, num2):
        # Метод для выполнения умножения
        return num1 * num2

    def perform_square(self, num):
        # Метод для вычисления квадрата числа с использованием MathOperation
        return self.math_operation._square(num)

    def perform_cube(self, num):
        # Метод для вычисления куба числа с использованием MathOperation
        return self.math_operation._cube(num)

    def perform_factorial(self, num):
        # Метод для вычисления факториала числа с использованием MathOperation
        return self.math_operation._factorial(num)

# Пример использования классов
math_op = MathOperation()
calc = Calculator(math_op)

result_add = calc.add(5, 3)
result_subtract = calc.subtract(10, 7)
result_multiply = calc.multiply(4, 6)
result_square = calc.perform_square(4)
result_cube = calc.perform_cube(3)
result_factorial = calc.perform_factorial(5)

print("Сложение:", result_add)
print("Вычитание:", result_subtract)
print("Умножение:", result_multiply)
print("Квадрат:", result_square)
print("Куб:", result_cube)
print("Факториал:", result_factorial)