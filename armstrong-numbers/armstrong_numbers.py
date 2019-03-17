import math


def is_armstrong(number):
    digits = map(lambda x: int(x), list(str(number)))
    number_of_digits = len(digits)
    return number == sum(map(lambda d: math.pow(d, number_of_digits), digits))
