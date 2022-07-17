import sys
from termcolor import colored
from inputmanager import InputManager
from deck import Deck
from card import Card
from suits import Suits

class Player(object):
    def __init__(self, bank):
        self.bank = bank
        self.deck = Deck.shuffled()
        self.wager = 5
    
    def set_deck(self, deck):
        self.deck = deck

    def can_afford_round(self):
        if self.bank >= self.wager:
            return True
        else:
            return False

    def bank_balance(self):
        return int(self.bank)

    def play_one_round(self):
        choice = None
        while (not choice):
            if self.bank > 1:
                print(f'You have {self.bank_balance()} dollars in the bank and are wagering {self.wager} dollars.\n')
            else:
                print(colored('You are broke!!!', 'red'))
                sys.exit(0)
            
            if self.can_afford_round():
                choice = InputManager.get_choice(['Category', 'Card', 'Probabilities', 'Wager', 'Quit'])
                if choice == 'Category':
                    choice = InputManager.get_choice({'face': 'Face card', 'red': 'Red card', 'black': 'Black card', 'suit': 'Suit'})
                    if choice == 'Suit':
                            choice = InputManager.get_choice(Suits.all())
                elif choice == 'Card':
                    choice = InputManager.get_choice(Card.value_range())
                elif choice == 'Probabilities':
                    print(self.deck.probabilities())
                    choice = None
                elif choice == 'Wager':
                    self.wager = InputManager.get_numeric_input("Enter a wager in dollars: ", self.bank_balance())
                    choice = None
                else:
                    sys.exit(0)
            else:
                print(colored(f'Your wager of {self.wager} exceeds your balance of {self.bank_balance()}!', 'red'))
                self.wager = InputManager.get_numeric_input("Enter a wager in dollars: ", self.bank_balance())

        winners = []
        if choice == 'face':
            winners = self.deck.facecards
        elif choice == 'red':
            winners = self.deck.red
        elif choice == 'black':
            winners = self.deck.black
        elif choice in Suits.all():
            winners = self.deck.by_suit[choice]
        else:
            winners = self.deck.by_value[choice]

        odds = (self.deck.calc_probability(winners) + 100) / 100
        c = self.deck.peek()
        
        if c in winners:
            print(colored(f'{c.name_and_suit()} - You win {round(self.wager * odds, 2)} dollars!', 'green'))
            self.bank += self.wager * odds
        else:
            print(colored(f'{c.name_and_suit()} - You lose {self.wager} dollars.', 'red'))
            self.bank -= self.wager
        self.deck.pop()