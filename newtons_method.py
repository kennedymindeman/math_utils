from dataclasses import dataclass


@dataclass
class Term:
    coefficient: float
    power: float


@dataclass
class Function:
    terms: list[Term]


def newtons_method(guess, function, iterations):
    for _ in range(iterations):
        guess = iterate_root_guess(guess, function)

    return guess


def iterate_root_guess(guess, function):
    derivative = differentiate(function)
    value_at_guess = evaluate(guess, function)
    slope_at_guess = evaluate(guess, derivative)
    return guess - value_at_guess / slope_at_guess


def differentiate(function: Function):
    def diff_term(term: Term):
        if term.power == 0:
            raise NotImplementedError

        return Term(term.coefficient * term.power, term.power - 1)

    terms = [diff_term(term) for term in function.terms if term.power != 0]
    return Function(terms)


def evaluate(x_input, function: Function):
    def evaluate_term(term: Term):
        return term.coefficient * (x_input**term.power)

    return sum(evaluate_term(term) for term in function.terms)
