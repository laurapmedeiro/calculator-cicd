import app, math


class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        if x == 0 and y < 0:
            return float('inf')
        self.check_types(x, y)
        return x ** y
    
    def square(self, x):
        self.check_types(x,2)
        return math.sqrt(x)

    def log10(self, x):
        if x < 0:
            raise TypeError("Logarithm in base 10 cannot be calculated to negative numbers")
        if x == 0:
            return -float('inf')
        self.check_types(x,10)
        return math.log10(x)
    
    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    print(calc.add(2, 2))
    print(calc.power(0,-2))
    print(calc.power(0,2))
    print(calc.log10(0))
