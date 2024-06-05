from HandRank import HandRank


class Hand:

    def __init__(self, card_list):
        self.card_list = card_list.sort(key=lambda x: x.value, reverse=True)
        self.values = self.get_values(card_list)
        self.suits = self.get_suits(card_list)
        self.hand_rank = HandRank
        self.hand_value = 0

    @staticmethod
    def get_values(card_list):
        card_values = []
        for card in card_list:
            card_values.append(card.value)

        return card_values

    @staticmethod
    def get_suits(card_list):
        card_suits = []
        for card in card_list:
            card_suits.append(card.suit)

        return card_suits
