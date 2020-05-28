class Calculator:

    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

calculator = Calculator(10, 2)
print(calculator.sum())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())