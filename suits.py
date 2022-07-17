class Suits(object):
    @staticmethod
    def red():
        return ['Hearts', 'Diamonds']

    @staticmethod
    def black():
        return ['Spades', 'Clubs']

    @staticmethod
    def all():
        return Suits.red() + Suits.black()
