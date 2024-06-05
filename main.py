from re import split
from Card import Card
from Hand import Hand
from Play import evaluate_hand


if __name__ == '__main__':
    player_one_wins_count = 0   # Overall counter of player 1 wins

    # Read in poker hands from file
    file = open('Poker.txt', 'r')
    lines = file.readlines()

    # Each line contains one round of poker hands, first five "cards" are player 1, second five are player 2
    for line in lines:
        cardList = split(" ", line)

        # Convert string representation of card into a Card object, adding the first five
        # cards to player 1 and the second five to player 2
        player_one_cards = []
        player_two_cards = []
        for c in range(0, 10):
            card = Card(cardList[c])
            if c < 5:
                player_one_cards.append(card)
            else:
                player_two_cards.append(card)

        # Create Hands for player 1 and player 2 from list of Card objects
        p1 = Hand(player_one_cards)
        p2 = Hand(player_two_cards)

        # Evaluate each players hand for rank and value
        evaluate_hand(p1)
        evaluate_hand(p2)

        # Determine the winner
        if p1.hand_rank.value > p2.hand_rank.value:
            player_one_wins_count += 1
        elif p1.hand_rank.value == p2.hand_rank.value and p1.hand_value > p2.hand_value:
            player_one_wins_count += 1
        elif p1.hand_rank.value == p2.hand_rank.value and p1.hand_value == p2.hand_value:
            for val in range(0, 5):
                if p1.values[val] > p2.values[val]:
                    player_one_wins_count += 1
                    break
                elif p1.values[val] < p2.values[val]:
                    break

    print(player_one_wins_count)
