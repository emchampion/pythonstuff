#knock knock joke

name = raw_input("What is your name?")
'''simple test to make sure they start they inputs and dont try to enter something else'''
#storage list for first letter checks
wouldLike = ['Y', 'y']
whoThere = ['W', 'w']
repeat = ['R', 'r']
#enter name and checks to make sure something was entered and it was not a number
if len(name) > 0 and name.isalpha():
    question = raw_input("Hello %s, would you like to hear a Knock Knock joke?" % name)
    answer = question[0]
else:
    print 'Are you trying to trick me? You entered a nothing or a number!'
#pulls the first letter of the "whos there"


if answer in wouldLike:
    knock = raw_input("Knock Knock...")
    knocktest = knock[0]
    if len(knocktest) > 0 and knocktest in whoThere:
        repeatWho = raw_input("Repeat...")
        whowho = repeatWho[0]
        if len(whowho) > 0 and whowho in repeat:
            print "Who Who!"
        else:
            print "You did not say 'Repeat who?'"
    else:
        print 'You did not say "Who\'s there?"'
else:
    print "That\'s a shame I had a good joke for you."
