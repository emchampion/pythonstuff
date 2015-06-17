#change maker
#takes inputs
price = raw_input("Item Price: ")
paid = raw_input("Tendered cash: ")
#allows for decimal point inputs and converts them to floatinpoint
price = float(price)
paid = float(paid)
change = int((paid - price) * 100)
changecoin = float(paid - price)

#prints change
print ("Price: %.2f" % price)
print ("Paid: %.2f" % paid)
print ('Change: %.02f' % changecoin)
print ("Change left: %s" % change)

# How many 20s
if change >= 2000:
    print "Twenties: %s" % (change / 2000)
    change = (change % 2000)
else:
    print "Twenties: 0"
# 10s
if change >= 1000:
    print "Tens: %s" % (change / 1000)
    change = (change % 1000)
else:
    print "Tens: 0"
# 5s
if change >= 500:
    print "Fives: %s" % (change / 500)
    change = (change % 500)
else:
    print "Fives: 0"
# 1s
if change >= 100:
    print "Ones: %s" % (change / 100)
    change = (change % 100)
else:
    print "Dollars: 0"
#.25c
if change >= 25:
    print "Quarters: %s" % (change / 25)
    change = (change % 25)
else:
    print "Quarters: 0"
#.10c
if change >= 10:
    print "Dimes: %s" % (change / 10)
    change = (change % 10)
else:
    print "Dimes: 0"
#.05c
if change >= 5:
    print "Nickles: %s" % (change / 5)
    change = (change % 5)
else:
    print "Nickles: 0"
#.01c
if change >= 1:
    print "Pennies: %s" % (change / 1)
    change = (change % 1)
else:
    print "Pennies: 0"
