import random
from re import S
from tabulate import tabulate
from suits import Suits
from card import Card 

# A class to represent one or more decks of cards
class Deck(object):
    # Factory for a shuffled deck
    @classmethod
    def shuffled(cls, count=1):
        return cls(True, count)
    
    # Factory for an unshuffled deck
    @classmethod
    def factory_fresh(cls, count=1):
        return cls(False, count)

    def __init__(self, shuffled, count=1):
        self.cards = []
        self.red = []
        self.black = []
        self.facecards = []
        self.by_value = {}
        self.by_suit = {}

        # store cards in appropriate bins for performance reasons
        card_value_range = Card.value_range()
        for v in card_value_range:
            self.by_value[v] = []
        for s in Suits.all():
            self.by_suit[s] = []

        for r in range(0,count):
            for s in Suits.all():
                for v in card_value_range:
                    card = Card(v, s)
                    self.cards.append(card)
                    self.by_value[v].append(card)
                    self.by_suit[s].append(card)

                    if card.is_red():
                        self.red.append(card)
                    else:
                        self.black.append(card)
                    if card.is_facecard():
                        self.facecards.append(card)

        if(shuffled):
            random.shuffle(self.cards)

    def len(self):
        return len(self.cards)

    # peek at the next card in the deck without removing it
    def peek(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards[0]

    # pop the next card from the deck
    def pop(self):
        c = self.cards.pop(0)
        if (c.is_facecard()):
            self.facecards.remove(c)
        if (c.is_red()):
            self.red.remove(c)
        else:
            self.black.remove(c)
        self.by_value[c.value].remove(c)
        self.by_suit[c.suit].remove(c)
        return c

    # calculate a specific probability
    def calc_probability(self, p, rnd=1):
        l1 = len(p)
        l2 = len(self.cards)
        return round(l1 / l2 * 100, rnd)

    # display all probabilities to the user in a nice format
    def probabilities(self):
        data = []
        card_value = 13
        data.append(["Face Card", self.calc_probability(self.facecards), Card.name(card_value), self.calc_probability(self.by_value[card_value])])
        card_value -= 1
        data.append(["Red Card", self.calc_probability(self.red), Card.name(card_value), self.calc_probability(self.by_value[card_value])])
        card_value -= 1
        data.append(["Black Card", self.calc_probability(self.black), Card.name(card_value), self.calc_probability(self.by_value[card_value])])
        card_value -= 1
        for s in Suits.all():
            data.append([s, self.calc_probability(self.by_suit[s]), Card.name(card_value), self.calc_probability(self.by_value[card_value])])
            card_value -= 1
        while(card_value > 0):
            data.append(["", "", Card.name(card_value), self.calc_probability(self.by_value[card_value])])
            card_value -= 1

        return tabulate(data, headers=["Category", "Probability", "Card", "Probability"]) + "\n"

    def __str__(self):
        return f"Deck([{self.len()} Cards])"
