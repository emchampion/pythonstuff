#!/usr/bin/env python
""" crypto.py
    Implements a simple substitution cypher
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"
    #menu called by the main
def menu():
    response = raw_input(" 0) Quit \n 1) Encode \n 2) Decode \n")
    return response
#counts where it is at in the alpha and prints from the key
def encode(var1):
    final = " "
    var1 = var1.upper()
    for x in range(0, len(var1)): #loops for the range of the var1
        for y in range(0, len(alpha)): #loops through to check characters
            findx = var1[x].find(alpha[y]) #finds the equivilant from the alpha
            if findx != -1:
                foundx = y
        final = "{1}".format(foundx,key[foundx])
        print final #prints the results as it loops one character at a time
    return
#takes leters from the key and prints them from the alpha
def decode(var2):
    final = " "
    var2 = var2.upper()
    for x in range(0, len(var2)): #loops for the range of the var2
        for y in range(0, len(key)):
            findx = var2[x].find(key[y]) #finds the equivilant from the key
            if findx != -1:
                foundx = y
        final = "{1}".format(foundx,alpha[foundx])
        print final
    return
#main that lets us select what to do   
def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = raw_input("text to be encoded: ")
      print encode(plain)
    elif response == "2":
      coded = raw_input("code to be decyphered: ")
      print decode(coded)
    elif response == "0":
      print "Thanks for doing secret spy stuff with me."
      keepGoing = False
    else:
      print "I don't know what you want to do..."
    return
      
main()
