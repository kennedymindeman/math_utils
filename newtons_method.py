def iterate_root_guess(guess, function, derivative):
    return guess - function(guess) / derivative(guess)
