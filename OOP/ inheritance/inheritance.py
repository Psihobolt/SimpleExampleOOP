class A:
    @staticmethod
    def addition(left, right):
        return left + right

    @staticmethod
    def subtraction(left, right):
        return left - right


class B(A):
    @staticmethod
    def multiply(left, right):
        return left * right

    @staticmethod
    def division(left, right):
        return left / right


# Родительский класс может только сложить и вычесть 2 числа
print(f'Result with method "{A.addition.__name__}" in A class = {A.addition(20, 10)}')
print(f'Result with method "{A.subtraction.__name__}" in A class = {A.subtraction(20, 10)}')

# Родительский класс может только сложить и вычесть 2 числа
print(f'Result with method "{B.addition.__name__}" in B class = {B.addition(15, 10)}')
print(f'Result with method "{B.subtraction.__name__}" in B class = {B.subtraction(15, 10)}')
print(f'Result with method "{B.multiply.__name__}" in B class = {B.multiply(15, 10)}')
print(f'Result with method "{B.division.__name__}" in B class = {B.division(15, 10)}')
