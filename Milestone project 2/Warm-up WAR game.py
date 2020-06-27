# Card Class

import random
suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten','Jack', 'Queen', 'King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 11, 'Queen': 12, 'King': 13,'Ace': 14}
# Suit, Rank, value of the Card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __strg__ (self):
        return self.rank + "of " + self.suit
# example: two_hearts = Card ("Hearts", "Two")
# print(two_hearts) : 2 string so we need to associate a number to the rank for the comparison

# Deck class
class Deck:
    def __init__ (self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
            # Create the Card object
                created_card = Card (suit, rank)
                self.all_cards.append(created_card)
# example: new_deck =Deck()
# new_deck.all_cards[] (provide where in the memory in the computer)
# first_card = new_deck.all_cards[0] (grab the 1st card)
# print(first_card)
# or call all cards
# for card_object in new_deck.all_cards:
#   print(card_object)
# Shuffle the cards
    def shuffle(self):
        random.shuffle(self.all_cards)
 # Need to remove the card that has been played
    def deal_one(self):
        return self.all_cards.pop()
# Player
class Player:
    def __init__ (self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards (self, new_cards):
        if type(new_cards) == type ([]):
            self.all_cards.extend (new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__ (self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# Game set-up
# Create Players
player_one = Player('One')
player_two = Player('Two')
# Create the new deck
new_deck = Deck()
new_deck.shuffle()
# split the deck
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num =0
while game_on:

    round_num+= 1
    print(f"Round{round_num}")
# Check if someone does not have cards anymore
    if len(player_one.all_cards) == 0:
        print('Player One  lost!')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two lost!')
        game_on = False
        break
    else:
# STart a New round
        player_one_cards=[]
        player_one_cards.append(player_one.remove_one())
        player_two_cards=[]
        player_two_cards.append(player_two.remove_one())

    at_war =True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war= False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war= False
        else:
            print('WAR!')

            if len(player_one.all_cards) <5:
                print("Player one unable to declare war, so Player Two wins!")
                game_on = False
                at_war = False
            elif len(player_two.all_cards) <5:
                print("Player two unable to declare war, so Player One wins!")
                game_on = False
                at_war = False
            else:
                for num in range (5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())