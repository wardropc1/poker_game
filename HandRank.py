from enum import Enum


class HandRank(Enum):
    high_card = 0
    one_pair = 1
    two_pairs = 2
    three_of_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_kind = 7
    straight_flush = 8
    royal_flush = 9
