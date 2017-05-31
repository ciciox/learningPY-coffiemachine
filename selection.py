confirm = ('')

def Selection():
    import time
    #print('Press:')
    #time.sleep(1)
    mylist = ['1. For Espresso','2. For Double Espresso','3. For Americano','4. For Cappuccino']
    print("\n".join(mylist))
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
    ## manage unexected value return to the begin of IF

    print('You have selected ',sel)
    print('Please press "Y" to confirm')
    confirm = input()
    print( 'is 1 ',confirm )
    #return confirm
    ### after the return the bariable is not worling

    print( 'is 2',confirm )
    #restart point


def ConfirmSel(): ## this function is not working ## is not getting the Return
    #from selection import Selection(confirm)

    import time
    print( 'is 3',confirm )
    if 'y' in confirm:
    #if confirm == yes:
    #if confirm == 'y' or 'Y':
        print('Your coffie is in preparation')
        time.sleep(1)
        print('Please Wait')
    else:
        print ("Your selection hasn't been recognise ")
        print('Please make again your choose')
        #exit()
