from pprint import pprint

shuffledCards = []

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck():
    def __init__(self):
        self.cards = []
        value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suit = ['hearts', 'diamonds', 'clubs', 'spades']
        for i in range(len(suit)):
            print("appending suit")
            for j in range(len(value)):
                print("appending value")
                print(str(Card(i, j)))
                self.cards.append(Card(i, j))

test = Deck()
pprint(vars(test))
