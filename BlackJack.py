from random import shuffle

class Blackjack:
 values={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
  
 def play(self):
  '''play a game'''   
  d = GameOfCards()
  d.mix()
  bank = Hand('Bank')
  player = Hand('Player')

  # gives two cards to the player and two to the bank
  for i in range(2):  
    player.addCard(d.getCard())
    bank.addCard(d.getCard())

  # show the hands
  bank.showHand()
  player.showHand()

  # as long as the player ask for a Card!, The bank gets cards
  response = input('Would you like another Card? Yes or No? (By default Yes) ')
  while response in ['','y','Y','yes','YES','Yes']:
    c = d.getCard()
    print("You have:")
    print(c)
    player.addCard(c)
    if self.total(player) > 21:
       print("You have passed 21. You have lost.")
       return   
    response = input('Card? Yes or No? (by default Yes) ')

  # the bank play with those rules  
  while self.total(bank) < 17:
    c = d.getCard()
    print("The bank has:")
    print(c)
    bank.addCard(c)
    if self.total(bank) > 21:
       print("The bank has passed 21. You have won.")
       return

  # if 21 is has not been passed, compare the hands to find the winner  
  self.compare(bank, player)

      
 def total(self, hand):
    ''' (Hand) -> int
    calculate the sum of all the cards' values in the hand
    '''
    total = 0
    flag = 0
    for i in range(len(hand.hand)): #scan hand for cards of Face Value
        if hand.hand[i].value == 'A':
            total += 11
            flag += 1
        elif hand.hand[i].value == 'J' or hand.hand[i].value == 'Q' or hand.hand[i].value == 'K':
            total += 10
        else:
            total += int(hand.hand[i].value)#if no facevalue otherwise it is a 1-10 card and just add 1-10 to the total
    if total > 21: #if total is greater than 21
        while flag > 0: #check if there are aces in hand
            total -= 10 #if there are subtract 10 for each ace
            flag -=1
        
    return total
     

 def compare(self, bank, player):
    ''' (Hand, Hand) -> None
    Compare the Hand of the player with the hand of the bank
    and display the messages
    '''
    flag1 = None #ace flag for player 
    flag2 = None #j,q, or k flag for player
    flag3 = None #ace flag for bank
    flag4 = None #j,q, or k flag for bank
    b_j_p = 0 #black jack player
    b_j_b = 0 #black jack bank
    
    if self.total(bank) > self.total(player): #if total of bank is more than the player, player loses
        print('You have lost.')
    elif self.total(bank) < self.total(player): #if total of bank is less than the player, player wins 
        print('You have Won.')
    elif self.total(bank) == self.total(player): #if the total of the bank is equal to the player then check the hand for the other 3 cases
        black_jack_p, black_jack_b = 0,0
        for i in range(len(player.hand)): #check hand of player to see if there is a blakc jack(ace + J, K or Q)
            if player.hand[i].value == 'A':
                flag1 = True
            elif player.hand[i].value == 'J' or  player.hand[i].value == 'Q' or  player.hand[i].value == 'K':
                flag2 = True     
        for j in range(len(bank.hand)): #check hand of bank to see if there is a blakc jack(ace + J, K or Q)
            if bank.hand[i].value == 'A':
                flag3 = True
            elif bank.hand[i].value == 'J' or  bank.hand[i].value == 'Q' or  bank.hand[i].value == 'K':
                flag4 = True 
        if flag1 == True and flag2 == True: #if player has an ace and a j,q or k player has black jack
            b_j_p= 1 
        if flag3 == True and flag4 == True: #if bank has an ace and a j,q or k bank has black jack
            b_j_b = 1
        if b_j_p == b_j_b: #if player and bank both have black jack it is a tie so print equaility
            print('Equality')
        elif b_j_p > b_j_b: #if player has a black jack and bank doesnt player wins so print players win cause of black jack
            print('The player wins because of black jack')
        elif b_j_p < b_j_b: #if bank has a black jack and player doesnt bank wins so print bank win cause of black jack 
            print('The bank wins because of black jack')
        else: #if neither player has black jack and they have the same total print equality because it is a tie
            print('Equality')
            
    # in case of equality, if the total is 21,  if the bank has a blackjack
    # display 'You have lost.'; if the playerer has a blackjack 'You have won.' 
    # otherwise, display 'Equality.'

       
class Hand(object):
    '''represents a Hand of cards to play'''

    def __init__(self, player):
        '''(Hand, str)-> none
        initializes the player's name and the card list with list being empty'''

        self.player = player
        self.hand = []

    def addCard(self, card):
        '''(Hand, Card) -> None
        add a card to the hand'''

        self.hand.append(card)
        

    def showHand(self):
        '''(Hand)-> None
        display the player's name and the hand'''
        print(self.player + ":", end=' ')
        for i in range(len(self.hand)):
            print(self.hand[i].value, self.hand[i].color, end=' ')
        print()         
    def __eq__(self, other):
        '''returns True if the hands have the same cards in the same order'''
        
        return self.hand == other.hand and self.player == other.player

    def __repr__(self):
        '''returns a representation of the object'''
        
        return(str(self.player) + ": ", self.hand.value, self.hand.color)

class Card:
    '''represente a card to play'''

    def __init__(self, value, color):
        '''(Card,str,str)->None        
        initializes the value and the color of the card'''
        self.value = value
        self.color = color  # spade, heart, club or diamond

    def __repr__(self):
        '''(Card)->str
        returns the representation of the object'''
        return 'Card('+self.value+', '+self.color+')'

    def __eq__(self, other):
        '''(Card,Card)->bool
        self == other if the value and color are the same'''
        return self.value == other.value and self.color == other.color

class GameOfCards:
    '''Represent the game of 52 cards'''
    # values and colors are variables of class
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    colors = ['\u2660', '\u2661', '\u2662', '\u2663']
    # colors is a set of 4 symbols Unicode that represents the 4 colors
    # spade, heart, club or diamond
    
    def __init__(self):
        'initializes the packet of 52 cards'
        self.packet = []          # packet is empty at the start
        for color in GameOfCards.colors: 
            for value in GameOfCards.values: # variables of the class
                # add a card of value and color
                self.packet.append(Card(value,color))

    def getCard(self):
        '''(GameOfCards)->Card
        distribute a card, the first from the packet'''
        return self.packet.pop()

    def mix(self):
        '''(GameOfCards)->None
        to mix the card game'''
        shuffle(self.packet)

    def __repr__(self):
        '''returns a representation of the object'''
        return 'Packet('+str(self.packet)+')'

    def __eq__(self, other):
        '''return True if the packets are the same cards in the same order'''
        return self.packet == other.packet
    
    
b = Blackjack()
b.play()

