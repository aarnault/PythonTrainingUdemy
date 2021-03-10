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
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has " + deck_comp

    def shuffle (self):
        random.shuffle(self.deck)

    def deal (self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards =[]
        self.value=0
        self.aces=0


    def add_card (self, card):
        self.cards.append(card)
        values[card.rank]
        self.value += values[card.rank]

        if card.rank == 'Aces':
            self.aces += 1

    def adjust_for_ace (self):
        #if total >21 and I still have an ace then change my ace to be a 1 instead
        while self.value > 21 and self.aces:
            # 0 is always treated as False so self.aces is the same than sel.aces  > 0
            self.value -= 10
            self.aces -=1

# test_deck = Deck()
#test_deck.shuffle()
#test_player = Hand()
#pulled_card = test_deck.deal()
#print(pulled_card)
#test_player.add_card(pulled_card)
#print(test_player.value)
#test_player.add_card(test_deck.deal()) and continue with the same to add more cards
class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet (self):
        self.total += self.bet

    def lose_bet(self):
        self.total += self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print ("Sorry please provide a number.")
        if chips.bet > chips.total:
            print("Sorry, you do not have enough chips! You have: {} .format(chips.total)")
        else:
            break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    while True :
        X =input('Hit or Stand? Enter h or s')

        if X[0].lower() == 'h':
            hit(deck, hand)
        elif X[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Please choose h or s")
            continue
        break

def show_some(player, dealer):
    print('Dealer hand:')
    print('one card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('Players hand:')
    for card in player.cards:
        print(card)
def show_all (player, dealer):
    print('Dealers hand:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Players hand:')
    for card in player.cards:
        print(card)

def player_bust(player, dealer, chips):
    print("Bust player!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_bust(player, dealer, chips):
    print("Player win dealer busted!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push (player, dealer):
    print('Dealer and Player tie! Push')


#Entire game

while True:
    print("Welcome to Blackjack!")

    #Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Set up the Player's chip
    player_chips = Chips()
    #Prompt the Player for their bet
    take_bet(player_chips)
    #Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    while playing: #recall this variable from our hit_or_stand function
        #Prompt for player to Hit or Stand
        hit_or_stand(deck, player_hand)
        #Show cards (but keep one dealer card hidden
        show_some(player_hand, dealer_hand)
        #If player's hand exceeds 21, run player_busts() and break out of the loop
        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break

        # if Player has not busted, player Dealer's hand until Dealer reaches 17
    if player_hand.value <=21:

        while dealer_hand.value <17:
            hit(deck, dealer_hand)

        # show all cards
        show_all(player_hand, dealer_hand)
        #Run different winning scenarios
        if dealer_hand.value >21:
            dealer_bust(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

        #Inform Player of their chips total
    print('\n Player total chips are at: {}'.format(player_chips.total))
        #Ask to play again
    new_game = input("Would you like to play again? y/n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing')
        break

