from newtons_method import Function, Term, differentiate


def test_differentiate():
    function = Function([Term(1, 3), Term(-1, 1), Term(1, 0)])
    derivative = Function([Term(3, 2), Term(-1, 0)])
    assert derivative == differentiate(function)
