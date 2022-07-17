from suits import Suits

class Card(object):
    @staticmethod
    def value_range():
        cards = {}
        for i in range(1, 14):
            cards[i] = Card.name(i)
        return cards

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

    def is_red(self):
        return self.suit in Suits.red()

    def is_black(self):
        return self.suit in Suits.black()

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