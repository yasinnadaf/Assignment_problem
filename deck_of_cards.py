import random


class Cards:
    def __init__(self):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = []

    def deck(self):
        """
        Function for shuffle and distribute cards
        """
        for p in range(4):
            player_cards = []
            for c in range(9):
                suffle = random.choice(self.suits)+" "+random.choice(self.ranks)
                player_cards.append(suffle)
            self.cards.append(player_cards)

    def print(self):
        """
        Function for printing cards
        """
        for i in self.cards:
            print("{0}".format(i), end='\n ')
        print()


if __name__ == '__main__':
    card = Cards()
    card.deck()
    card.print()

