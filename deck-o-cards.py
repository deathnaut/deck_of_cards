from pprint import pprint

shuffledCards = []

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck():
    def __init__(self):
        self.cards = []

    def createDeck(self):
        print("creating deck")
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        for i in suits:
            print("appending suit")
            for j in values:
                print("appending value")
                self.cards.append(Card(suits, values))
        return self

test = Deck()
deck = test.createDeck()
pprint(vars(test))
