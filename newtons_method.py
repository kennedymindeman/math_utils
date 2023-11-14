from dataclasses import dataclass


@dataclass
class Term:
    coefficient: float
    power: float


@dataclass
class Function:
    terms: list[Term]


def iterate_root_guess(guess, function, derivative):
    return guess - function(guess) / derivative(guess)


def differentiate(function: Function):
    def diff_term(term: Term):
        if term.power == 0:
            raise NotImplementedError

        return Term(term.coefficient * term.power, term.power - 1)

    terms = [diff_term(term) for term in function.terms if term.power != 0]
    return Function(terms)
