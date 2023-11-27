from armstrong import is_armstrong_number
from newtons_method import (
    Function,
    Term,
    differentiate,
    iterate_root_guess,
    newtons_method,
)


def test_differentiate():
    function = Function([Term(1, 3), Term(-1, 1), Term(1, 0)])
    derivative = Function([Term(3, 2), Term(-1, 0)])
    assert derivative == differentiate(function)


def test_iterate_root_guess():
    function = Function([Term(1, 3), Term(-1, 1), Term(1, 0)])
    guess = -1
    guess = iterate_root_guess(guess, function)
    assert guess == -1.5
    guess = iterate_root_guess(guess, function)
    assert guess == -1.3478260869565217
    guess = iterate_root_guess(guess, function)
    assert guess == -1.325200398950907


def test_newtons_method():
    function = Function([Term(1, 3), Term(-1, 1), Term(1, 0)])
    guess = -1
    root_approx = newtons_method(guess, function, 3)
    assert root_approx == -1.325200398950907


def test_armstrong_number():
    assert is_armstrong_number(153)
    assert is_armstrong_number(370)


def test_single_digit_numbers():
    for i in range(10):
        assert is_armstrong_number(i)


def test_non_armstrong_numbers():
    assert not is_armstrong_number(154)
    assert not is_armstrong_number(783)
