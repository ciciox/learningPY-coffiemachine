credit = 0
def Payment():
    global credit
    print('The cost for''is 1£')
    print('Please insert coin')
    credit = float(input())
    while credit < 1:
        print('Your credit now is', credit,'£')
        print('You still need to add other',-credit+1,'cent')
        newcredit = float(input())
        credit = newcredit + credit
    #return credit

# uncomment for debugging
Payment()
print(credit)
#print (credit)


def Change():

    ## need to be implemented ##
    return ()

