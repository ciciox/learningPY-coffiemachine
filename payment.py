
def Payment():
    print('The cost for''is 1£')
    print('Please insert coin')
    cash = float(input())
    while cash < 1:
        print('Your credit now is', cash,'£')
        print('You still need to add other',-cash+1,'cent')
        newcash = float(input())
        cash = newcash + cash

def Change():

    ## need to be implemented ##
    return ()

