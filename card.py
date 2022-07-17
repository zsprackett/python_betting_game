from suits import Suits

# This class represents a single card
class Card(object):
    # static method to get valid card ranges
    @staticmethod
    def value_range():
        cards = {}
        for i in range(1, 14):
            cards[i] = Card.name(i)
        return cards

    # static method to look up a card name from a card value
    @staticmethod
    def name(value):
        cards = {
            1: 'Ace',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }
        return cards[value]

    # boolean: returns true for red cards
    def is_red(self):
        return self.suit in Suits.red()

    # boolean: returns true for black cards
    def is_black(self):
        return self.suit in Suits.black()

    # boolean: returns true for face cards
    def is_facecard(self):
        return self.value > 10

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def name_and_suit(self):
        return f'{Card.name(self.value)} of {self.suit}'

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __str__(self):
        return self.name_and_suit()