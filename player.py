import sys
from termcolor import colored
from inputmanager import InputManager
from deck import Deck
from card import Card
from suits import Suits

# Represents a player
class Player(object):
    def __init__(self, bank):
        self.bank = bank
        self.deck = Deck.shuffled()
        self.wager = 5
    
    def set_deck(self, deck):
        self.deck = deck

    # Boolean: can the player afford to play at the current wager
    def can_afford_round(self):
        if self.bank >= self.wager:
            return True
        else:
            return False

    # Appropriately format money
    def format_money(self, money):
        return '{0:.2f}'.format(money)

    # Retrieve the bank account balance, properly formatted
    def get_bank_balance(self):
        return self.format_money(self.bank)

    # Retrieve the wager, properly formatted
    def get_wager(self):
        return self.format_money(self.wager)

    # Play a single round of the game
    def play_one_round(self):
        choice = None
        while (not choice):
            if self.bank > 1:
                print(f'You have ${self.get_bank_balance()} in the bank and are wagering ${self.get_wager()}.\n')
            else:
                print(colored('You are broke!!!', 'red'))
                sys.exit(0)
            
            if self.can_afford_round():
                choice = InputManager.get_choice(['Category', 'Card', 'Probabilities', 'Wager', 'Quit'])
                if choice == 'Category':
                    choice = InputManager.get_choice({'face': 'Face card', 'red': 'Red card', 'black': 'Black card', 'suit': 'Suit'})
                    if choice == 'suit':
                        choice = InputManager.get_choice(Suits.all())
                elif choice == 'Card':
                    choice = InputManager.get_choice(Card.value_range())
                elif choice == 'Probabilities':
                    print(self.deck.probabilities())
                    choice = None
                elif choice == 'Wager':
                    self.wager = InputManager.get_float_input("Enter a wager: ", self.get_bank_balance())
                    choice = None
                else:
                    sys.exit(0)
            else:
                print(colored(f'Your wager of {self.get_wager()} exceeds your balance of {self.get_bank_balance()}!', 'red'))
                self.wager = InputManager.get_float_input("Enter a wager: ", self.bank)

        # Check if the user won
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

        multiplier = (200 - self.deck.calc_probability(winners)) / 100
        c = self.deck.peek()
        
        if c in winners:
            winnings = round(self.wager * multiplier, 2)
            print(colored(f'{c.name_and_suit()} - You win ${self.format_money(winnings)} [{multiplier} multiplier]!', 'green'))
            self.bank += winnings
        else:
            print(colored(f'{c.name_and_suit()} - You lose ${self.get_wager()}.', 'red'))
            self.bank -= self.wager
        self.deck.pop()
