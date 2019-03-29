# Score categories
# Change the values as you see fit
from itertools import groupby

ONES = lambda ds: sum(d for d in ds if d == 1)
TWOS = lambda ds: sum(d for d in ds if d == 2)
THREES = lambda ds: sum(d for d in ds if d == 3)
FOURS = lambda ds: sum(d for d in ds if d == 4)
FIVES = lambda ds: sum(d for d in ds if d == 5)
SIXES = lambda ds: sum(d for d in ds if d == 6)
FULL_HOUSE = lambda ds: full_house(ds)
FOUR_OF_A_KIND = lambda ds: four_of_kind(ds)
LITTLE_STRAIGHT = (
    lambda ds:
    30
    if sorted(ds) == [1, 2, 3, 4, 5]
    else 0
)
BIG_STRAIGHT = (
    lambda ds:
    30
    if sorted(ds) == [2, 3, 4, 5, 6]
    else 0
)
CHOICE = lambda ds: sum(ds)
YACHT = (
    lambda ds:
    50
    if len(set(ds)) == 1
    else 0
)


def four_of_kind(ds):
    groups = [list(v) for k, v in groupby(sorted(ds))]
    group_of_4 = filter(lambda l: len(l) >= 4, groups)
    if len(group_of_4) == 1:
        return 4 * group_of_4[0][0]
    else:
        return 0


def full_house(ds):
    groups = [list(v) for k, v in groupby(sorted(ds))]
    lengths = map(lambda l: len(l), groups)
    if set(lengths) == {2, 3}:
        return sum(ds)
    else:
        return 0


def score(dice, category):
    return category(dice)
