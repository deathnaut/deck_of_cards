from pprint import pprint

# TODO: add shuffle deck functionality
shuffledCards = []

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "suit: {}, value: {}".format(self.suit, self.value)

class Deck():
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']

    def __init__(self):
        self.cards = []
        for i in range(len(Deck.suits)):
            for j in range(len(Deck.values)):
                card = Card(Deck.suits[i], Deck.values[j])
                self.cards.append(card)


test = Deck()
pprint(vars(test))
