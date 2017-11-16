from pprint import pprint

shuffledCards = []

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "suit: {}, value: {}\n".format(self.suit, self.value)

class Deck():
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
    suits = ['hearts', 'diamonds', 'clubs', 'spades']

    def __init__(self):
        self.cards = []
        print("creating deck")
        for i in range(len(Deck.suits)):
            print("appending suit")
            for j in range(len(Deck.values)):
                print("appending value", Deck.values[j])
                print(self.cards)
                card = Card(Deck.suits[i], Deck.values[j])
                self.cards.append(card)


test = Deck()
pprint(vars(test))
