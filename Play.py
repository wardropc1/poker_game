from HandRank import HandRank
import collections


def evaluate_hand(hand):

    if hand_has_royal_flush(hand):
        hand.hand_rank = HandRank.royal_flush
        hand.hand_value = 13  # ace
    elif hand_has_straight_flush(hand):
        hand.hand_rank = HandRank.straight_flush
        hand.hand_value = hand.values[0]  # highest value card
    elif (match := hand_has_four_of_kind(hand)) != 0:
        hand.hand_rank = HandRank.four_of_kind
        hand.hand_value = match
    elif hand_has_full_house(hand):
        hand.hand_rank = HandRank.full_house
        hand.hand_value = hand.values[0]  # highest value card
    elif hand_has_flush(hand):
        hand.hand_rank = HandRank.flush
        hand.hand_value = hand.values[0]  # highest value card
    elif hand_has_straight(hand):
        hand.hand_rank = HandRank.straight
        hand.hand_value = hand.values[0]  # highest value card
    elif (match := hand_has_three_of_kind(hand)) != 0:
        hand.hand_rank = HandRank.three_of_kind
        hand.hand_value = match
    elif (match := hand_has_two_pairs(hand)) != 0:
        hand.hand_rank = HandRank.two_pairs
        hand.hand_value = match
    elif (match := hand_has_one_pair(hand)) != 0:
        hand.hand_rank = HandRank.one_pair
        hand.hand_value = match
    else:
        hand.hand_rank = HandRank.high_card
        hand.hand_value = hand.values[0] # highest value card


# Ten, Jack, Queen, King, Ace, in same suit.
def hand_has_royal_flush(hand):
    royal_flush_values = [14, 13, 12, 11, 10]

    return hand.values == royal_flush_values and hand.suits.count(hand.suits[0]) == 5


# All cards are consecutive values of same suit
def hand_has_straight_flush(hand):
    return hand_has_flush(hand) and hand_has_straight(hand)


def hand_has_four_of_kind(hand):
    counter = collections.Counter(hand.values)
    match = 0

    for c in counter:
        if counter[c] > 3:
            match = c
    return match


# Three of a kind and a pair.
def hand_has_full_house(hand):
    set_of_three = 0
    counter = collections.Counter(hand.values)

    if max(counter.values()) == 3 and min(counter.values()) == 2:
        set_of_three = max(counter.keys())

    return set_of_three


# All cards of the same suit
def hand_has_flush(hand):
    counter = collections.Counter(hand.suits)
    return list(counter.values())[0] == 5


# All cards are consecutive values.
def hand_has_straight(hand):
    start_value = hand.values[0]
    for i in range(1, len(hand.values)):
        if hand.values[i] == start_value - 1:
            start_value -= 1
        else:
            return False

    return True


# Three of any value (e.g. 3 fours, 3 queens, etc.)
def hand_has_three_of_kind(hand):
    counter = collections.Counter(hand.values)
    match = 0

    for c in counter:
        if counter[c] > 2:
            match = c
    return match


# Check for two different pairs (must be exactly two pairs)
def hand_has_two_pairs(hand):
    pair_count = 0
    highest_pair = 0
    counter = collections.Counter(hand.values)

    for c in counter.values():
        if c == 2:
            pair_count += 1

    if pair_count == 2:
        highest_pair = max(counter.keys())

    return highest_pair


# Check for two cards of the same value
def hand_has_one_pair(hand):
    match_value = 0

    for i in range(4, 0, -1):
        if hand.values[i] == hand.values[i - 1]:
            match_value = hand.values[i]

    return match_value

