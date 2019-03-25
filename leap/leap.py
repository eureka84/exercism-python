def is_leap_year(year):
    return (is_divisible_by(4, year) and not is_divisible_by(100, year)) or is_divisible_by(400, year)


def is_divisible_by(divisor, number):
    return number % divisor == 0
