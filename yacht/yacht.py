# Score categories
# Change the values as you see fit
from itertools import groupby

ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(dice, category):
    if category == YACHT and all(map(lambda e: e == dice[0], dice)):
        return 50
    elif category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return sum(filter(lambda x: x == category, dice))
    elif category == FULL_HOUSE:
        sub_groups = get_sub_groups(dice)
        if set(map(lambda l: len(l), sub_groups)) == {2, 3}:
            return sum(dice)
        else:
            return 0
    elif category == CHOICE:
        return sum(dice)
    elif category == LITTLE_STRAIGHT and set(dice) == {1, 2, 3, 4, 5}:
        return 30
    elif category == BIG_STRAIGHT and set(dice) == {2, 3, 4, 5, 6}:
        return 30
    elif category == FOUR_OF_A_KIND:
        sub_groups = get_sub_groups(dice)
        groups_of_four_of_a_kind = [x for x in sub_groups if len(x) >= 4]
        if len(groups_of_four_of_a_kind) == 1:
            return sum(groups_of_four_of_a_kind[0][:4])
        else:
            return 0
    else:
        return 0


def get_sub_groups(dice):
    return [list(v) for k, v in groupby(sorted(dice))]
