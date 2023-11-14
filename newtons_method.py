from typing import Callable


def iterate_root_guess(guess: float, function: Callable, derivative: Callable) -> float:
    return guess - function(guess) / derivative(guess)
