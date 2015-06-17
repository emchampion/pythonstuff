#!/usr/bin/env python
# generate a random number
print "I will randomly generate a number and you can try to guess it."

import random                       #imports the random number module
numberGen = random.randint(1, 100)  #generates a number from 1-100

def begin():
    numberGen = random.randint(1, 100)  #generates a number from 1-100
    tries = 0
    while True:                         #loops until the number is picked
        guess = int(raw_input("Enter a number between 1 and 100: "))
        tries += 1
        if guess > numberGen:           #if the guess is to high
            print "Too High"
        elif guess < numberGen:         #if the guess is to low
            print "Too Low"
        else:
            print "Correct %s is the number" % numberGen    #you guessed right
            print "It took you %s tries" % tries
            break

def restart():                          #this lets up play again if we want to
    while True:
        again = int(raw_input(" 1) play again \n 2) quit \n"))  #1 for again 2 for im done
        if again == 1:
            begin()
        else:
            print "Goodbye"
            break

begin()
restart()
