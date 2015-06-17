pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower() #lowercases the word
first = word[0] #grabs the first letter of the word
vowl = ["a", "e", "i", "u"] #vowel list
new_word = word + pyg #the magic

if len(original) > 0 and original.isalpha():  #checks for letter characters
    if first in vowl: #checks for vowels
        print new_word
    else:               #if this goes we have a consonant
        new_word = word[1:] + first + pyg #rebuild of new_word for consonant
        print new_word
else:
    print 'Empty or a number, Try again!'
