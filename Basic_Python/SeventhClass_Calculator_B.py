class Calculator:

    def sum(self, value_a, value_b):
        return value_a + value_b

    def sub(self, value_a, value_b):
        return value_a - value_b

    def mul(self, value_a, value_b):
        return value_a * value_b

    def div(self, value_a, value_b):
        return value_a / value_b

calculator = Calculator()
print(calculator.sum(10, 2))
print(calculator.sub(4, 2))
print(calculator.mul(3, 3))
print(calculator.div(40, 10))