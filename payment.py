from core import *

def Payment(sel):
    global credit
    print('The cost for:',sel,'is 1£')
    print('Please insert coin')
    credit = float(input())
    while credit < 1:
        print('Your credit now is', credit,'£')
        print('You still need to add other',-credit+1,'cent')
        newcredit = float(input())
        credit = newcredit + credit
        print(credit)

# uncomment for debugging
#Payment()
#print (credit)

