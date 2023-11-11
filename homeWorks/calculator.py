class Calculator:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        self.a += int(other)

    def __sub__(self, other):
        self.a -= int(other)

    def __mul__(self, other):
        self.a *= int(other)

    def __truediv__(self, other):
        self.a /= int(other)

    def __str__(self):
        return f'{self.a}'

num = Calculator(3)
#num.__add__(3)
#num.__sub__(3)
#num.__mul__(3)
#num.__truediv__(3)