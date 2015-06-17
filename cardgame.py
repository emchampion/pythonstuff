#!/usr/bin/env python
 
""" cardGame.py
    basic card game framework
    keeps track of card locations for as many hands as needed
"""
import random
 
NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2
 
cardLoc = [0] * NUMCARDS
suitName = ("Hearts", "Diamonds", "Spades", "Clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", 
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("Deck", "Player", "Computer")
#clears out the deck
def clearDeck():
    #puts the number of cards (52) into the deck
    for d in range(NUMCARDS):
        cardLoc[d] == DECK
    print "Cards are in the Deck"
 
# defines the card names and shows who has them
def showDeck():
    print "#          Card          Location"
    card  = 0
    for cardNum in cardLoc:
        rank = card % 13
        suit = int(card / 13)
        card = card + 1
        print card, rankName[rank], "of", suitName[suit], playerName[cardNum]
#shows what is in the hand          
def showHand(USER):
    #shows cards in hand after assignment
    print " "
    print playerName[USER], "is holding the following:"
    for card in range(0,51):
        if cardLoc[card] == USER:
            rank = card % 13
            suit = int(card / 13)
            print card, rankName[rank], "of", suitName[suit]
#randomly assigns the card
def assignCard(USER):
    test = True
    #assings cards to players
    while test:
        card = random.randint(0, 51)
        if cardLoc[card] == DECK:
            cardLoc[card] = USER
            test = False
#the magic   
def main():
  clearDeck()
 
  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)
 
  showDeck()
  showHand(PLAYER)
  showHand(COMP)
 
 
main()
