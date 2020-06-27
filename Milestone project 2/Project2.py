import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__ (self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of "+ self.suit


class Deck:

    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                new_card= Card(suit, rank)
                self.deck.append(new_card)

    def __str__(self):
        new_deck = Deck()
        for all_cards in new_deck.deck:
            print(all_cards)

    def shuffle (self):
        random.shuffle(self.deck)

    def deal (self):
        return self.deck.pop()

class Hand:

    def __init__(self):
        self.cards =[]
        self.value=0
        self.aces=0
    def add_card (self, card):
        self.cards.append(card)
        for x in card:
            if self.suit = "Aces":
                adjust_for_ace (card)
                self.value.append(card)
            else:
                self.value.append(card)

    def adjust_for_ace (self):
        if self.suit == 'Aces':
            if self.value < 10:
                self.aces = 11
            else:
                self.aces = 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet (self):

    def lose_bet(self):


def take_bet():
    bet_value=




