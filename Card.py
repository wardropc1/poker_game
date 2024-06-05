class Card:

    def __init__(self, card):
        self.rank = card[0]  # first char in the string representation of a card
        self.value = self.assign_value(card)
        self.suit = card[1]  # second char in the string representation of a card

    @staticmethod
    def assign_value(card):
        switcher = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }
        return switcher.get(list(card)[0])


