
'''def ConfirmSel():
    #fix IF to get multiple
    confirm = Selection()
    value = ['y','yes','Y','YES']
    import time

    if confirm in value:
    #if confirm == yes:
    #if confirm == 'y' or 'Y':
        print('Your coffie is getting ready')
        time.sleep(1)
        print('Please Wait')
    else:
        print ("Your selection hasn't been recognise ")
        print('Please make again your choose')
        #### repite the IF
'''

def ConfirmSel():

    confirm = Selection()

    value = ['y','yes','Y','YES']
    import time
    print('Please press "Y" to confirm')
    confirm = input()
    while confirm is not value:

        if confirm in value:
        #if confirm == yes:
        #if confirm == 'y' or 'Y':
            print('Your coffie is getting ready')
            time.sleep(1)
            print('Please Wait')
            continue
        else:
            print ("Your selection hasn't been recognise ")
            print('Please make again your choose')
            print('Please press "Y" to confirm')
            confirm = input()

    else:
        print('Please press "Y" to confirm')
        confirm = input()





def Selection():
    import time
    print('Press:')
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
'''

    print('Please press "Y" to confirm')
    confirm = input()

    return confirm
'''


