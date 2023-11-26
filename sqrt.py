def sqrt(number):
    i = number

    while abs(i * i - number) > 8e-16:
        i = (i + number / i) / 2

    return i
