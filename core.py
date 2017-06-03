from payment import Payment

def Confirmation():
    import time
    from payment import Payment
    import payment

    #confirm = Selection()
    print('Please press "Y" to confirm or "N" to cancel')
    confirm = input().lower()
    value = ['y', 'yes']
    denyvalue = ['n', 'no']
    while confirm is not value:

        if confirm in value:
            Payment(sel)
            print('Please Wait')
            time.sleep(1)
            print('Your coffee is getting ready')
            time.sleep(1)
            break

        elif confirm in denyvalue:
            print('Please made again your choice')
            confirm = Selection()
            print('Please press "Y" to confirm')
            confirm = input().lower()
            value = ['y', 'yes']
            denyvalue = ['n', 'no']

        else:
                print ("Your selection hasn't been recognise ")
                print('Please make again your choose')
                print('Please press "Y" to confirm')
                confirm = input()
        break
    time.sleep(2)
    print('Your coffie now is Ready')
    print('Your remaining credit is', payment.credit - 1)
    time.sleep(1)
    print('Please collect your change and enjoy your drink')
    time.sleep(4)
    credit = 0

                #add handle exceptions


def Selection():
    import time
    print("Welcome,\nplease select a drink:")
    time.sleep(1)
    print('Press:')
    time.sleep(1)
    mylist = ['1. For Espresso','2. For Double Espresso','3. For Americano','4. For Cappuccino']
    print("\n".join(mylist))
    selection = int(input())  #this part create an exception if the value is not INT
    while selection != mylist:
        global sel
        if selection == 1:
            sel = "Espresso"
            break
        elif selection == 2:
            sel = "Double Espresso"
            break
        elif selection == 3:
            sel = "Americano"
            break
        elif selection == 4:
            sel = "Cappuccino"
            break
        else:
            try:
                print("Your selection hasn't been recognise ")
                print('Please make again your choose:')
                print("\n".join(mylist))
                continue
            #### this part of the except is not working
            except ValueError:
                print('value error 2')
    print('You have selected',sel)




