from functions import Function


def newtons_method(guess, function, num_iterations):
    for _ in range(num_iterations):
        guess = iterate_root_guess(guess, function)

    return guess


def iterate_root_guess(guess, function: Function):
    derivative = function.differentiate()
    value_at_guess = function.evaluate(guess)
    slope_at_guess = derivative.evaluate(guess)
    return guess - value_at_guess / slope_at_guess
