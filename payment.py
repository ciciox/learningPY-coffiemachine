def Payment():
    import selection
    global credit
    print('The cost for it is 1£')
    print('Please insert coin')
    credit = float(input())
    while credit < 1:
        print('Your credit now is', credit,'£')
        print('You still need to add other',-credit+1,'cent')
        newcredit = float(input())
        credit = newcredit + credit


# uncomment for debugging
#Payment()
#print (credit)
