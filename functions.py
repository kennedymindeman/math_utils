from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class TermABC:
    def __init__(self):
        raise ValueError

    def evaluate(self, x):
        raise ValueError

    def differentiate(self) -> TermABC:
        raise ValueError

    def is_constant(self) -> bool:
        raise ValueError

@dataclass(frozen=True)
class PolynomialTerm(TermABC):
    # coefficient: Rational | int
    # power: Rational | int
    coefficient: int
    power: int

    def evaluate(self, x):
        return self.coefficient * (x ** self.power)

    def differentiate(self):
        if self.coefficient == 0:
            raise NotImplementedError

        return PolynomialTerm(self.coefficient * self.power, self.power - 1)

    def is_constant(self):
        return self.power == 0


@dataclass(frozen=True)
class Function:
    terms: tuple[TermABC,...]

    def evaluate(self, x):
        return sum(term.evaluate(x) for term in self.terms)

    def differentiate(self):
        return Function(tuple(term.differentiate() for term in self.terms if not term.is_constant()))
