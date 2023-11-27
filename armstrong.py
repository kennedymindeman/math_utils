def is_armstrong_number(number):
    digits = []
    original_number = number

    while original_number:
        digits.append(original_number % 10)
        original_number //= 10

    return sum(digit ** len(digits) for digit in digits) == number
