class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for _ in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result

    def modulo(self, a, b):
        while a >= b:
            a = a - b
        return a
