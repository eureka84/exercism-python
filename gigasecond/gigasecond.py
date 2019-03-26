import math
from datetime import timedelta

giga_seconds = timedelta(seconds=math.pow(10, 9))


def add_gigasecond(moment):
    return moment + giga_seconds
