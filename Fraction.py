class Fraction:
    def __init__(self,numerator,denominator):
        self.num = numerator
        self.den = denominator
    def __str__(self):
        return f"{self.num}/{self.den}"
    def __float__(self):
        return self.num / self.den
    def reciprocal(self):
        return Fraction(self.den,self.num)
    def __add__(self, other):
        result_float = float(self) + float(other)
        num,den = result_float.as_integer_ratio()
        return Fraction(num,den)
    def __sub__(self, other):
        result_float = float(self) - float(other)
        num,den = result_float.as_integer_ratio()
        return Fraction(num,den)