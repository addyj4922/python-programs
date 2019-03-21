import random
suits=('Hearts','Diamonds','Spades','Clubs')
ranks_key=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':11, 'King':12, 'Ace':11}
playing= True

class Card():
    def __init__(self,suit, rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank +" of "+self.suit


class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks_key:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp= ''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return "The Deck has: "+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card=self.deck.pop()
        return single_card
'''
test_deck=Deck()
test_deck.shuffle()
print(test_deck)
'''

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0  #attribute to keep track of aces

    def add_cards(self,card):
        #card passsed in
        #from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        self.value+=values[card.rank]
        #track our aces
        if card.rank=='Ace':
            self.aces+=1

    def adjust_for_ace(self):
        #if  total value > 21 and i still hae an ace
        #then change my ace to be a 1 instead of an 11
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1


class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

'''
test_deck=Deck()
test_deck.shuffle()
#player
test_player=Hand() 
#deal 1 card from the deck Card(suit,rank)
pulled_card=test_deck.deal()
print(pulled_card)
test_player.add_cards(pulled_card)
print(test_player.value)
'''

def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("How many chips would you like to bet"))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet> chips.total:
                print("Sorry, you don't have enough Chips! You have {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    single_card= deck.deal()
    hand.add_cards(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing #to control an upcoming while loop
    while True:
        x=input("Hit or Stand? Enter h or s")
        if x[0].lower()== 'h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("Player stands dealer's Turn")
            playing= False
        else:
            print("Sorry i did not understand that, Please enter h or s")
            continue
        break
def show_some(player,dealer):
    print("\nDealer's Hand: ")
    print("<card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player,dealer,chips):
    print("\nPLAYER BUSTED!! DEALER WINS!\n")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("\nPLAYER WINS!\n")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("\nPLAYER WINS! DEALER BUSTED!\n")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("\nDEALER WINS!\n")
    chips.lose_bet()

def push(player,dealer):
    print('\nDealer and Player Tie! PUSH\n')

while True:
    print("Welcome to BLACKJACK!")
    #create & shuffle the deck, deal 2 cards to each player
    deck=Deck()
    deck.shuffle()

    #add cards to player's hand
    player_hand=Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())

    #add cards to dealers hand
    dealer_hand=Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())

    #set up chips for the player
    player_chips=Chips()

    #prompt the player for their bet
    take_bet(player_chips)

    #show cards (but keep one dealer card hidden
    show_some(player_hand,dealer_hand)

    while playing:
        #prompt player to hit or stand
        hit_or_stand(deck,player_hand)

        #show cards (but keep one dealer card hidden
        show_some(player_hand,dealer_hand)

        #if player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    #if the player hasn't busted, Play Dealer's hand until dealer reached 17
    if player_hand.value<=21:
        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)

            #show all cards
        show_all(player_hand,dealer_hand)

        #run different winning scenarios:
        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)

    #inform player of their total chips
    print("Player's total Chips are= {}".format(player_chips.total))
    #ask player to play again
    new_game=input("Do you want to play again? y/n")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thank you for playing :)")
        break