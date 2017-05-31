
def Payment():
    print('The cost for''is 1£')
    print('Please insert coin')
    cash = float(input())
    ## payment is not working need to add the count to the main cash variable
    while cash < 1:
        print('The total is', cash,'£')
        print('You need to add more money')
        cash = float(input() + cash)
        return (cash)
    else:
        print('caffe')

    return ()

def Change():
    return ()

Payment()