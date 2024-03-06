from rationals import Rational


def test_gcd():
    test_cases = {
        (38, 102): 2,
    }

    for test_case, expected in test_cases.items():
        assert Rational._gcd(*test_case) == expected


def test_lhs_multiplication():
    test_cases = {
        (Rational(1, 2), 1) : Rational(1, 2),
        (Rational(1, 2), 2) : 1,
    }

    for test_case, expected in test_cases.items():
        a, b = test_case
        breakpoint()
        assert a * b == expected
