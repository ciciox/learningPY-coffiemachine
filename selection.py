
def selectcoffie():
    selection = int(input ())

    if selection == 1:
        sel = "Espresso"
    elif selection == 2:
        sel = "Double Espresso"
    elif selection == 3:
        sel = "Americano"
    elif selection == 4:
        sel = "Cappuccino"
    else:
        print ("Your selection hasn't been recognise ")
        print('Please make again your choose')


    print('You have selected ', sel)
    print('Please press "Y" to confirm')

    confirm = input()
    #restart point

def confirmsel():
    if confirm == ('y'):
        print('Your coffie is in preparation')
        time.sleep(1)
        print('Please Wait')
    elif confirm == ('Y'):
        print('Your coffie is in preparation')
        time.sleep(1)
        print('Please Wait')
    else:
        print ("Your selection hasn't been recognise ")
        print('Please make again your choose')