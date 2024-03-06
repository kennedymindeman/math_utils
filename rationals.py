from dataclasses import dataclass


@dataclass(frozen=True)
class Rational:
    numerator: int
    denominator: int

    def evalutate(self):
        return self.numerator / self.denominator

    def __mul__(self, other):
        if type(other) is int:
            result = Rational(self.numerator * other, self.denominator)
            return result.reduced()

        if type(other) is Rational:
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            result = Rational(numerator, denominator)
            return result.reduced()

    def __rmul__(self, other):
        return self.__mul__(other)

    @staticmethod
    def _gcd(a, b):
        """Returns the greatest commond divisor of the inputs"""
        if b > a:
            a, b = b, a

        while a % b != 0:
            a, b = b, a % b

        return b

    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        if type(other) == int:
            return self.denominator == 1 and self.numerator == other

        if type(other) == Rational:
            return all([
            self.numerator == other.numerator,
            self.denominator == other.denominator,
        ])

        raise TypeError

    def reduced(self):
        gcd = self._gcd(self.numerator, self.denominator)
        return Rational(self.numerator // gcd, self.denominator // gcd)
