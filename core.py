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

        elif confirm in denyvalue:  # here something wrong
            print('Please made again your choice')
            confirm = Selection()
            print('Please press "Y" to confirm', sel, 'or "N" to cancel')
            confirm = input().lower()
            value = ['y', 'yes']
            denyvalue = ['n', 'no']

        else:
                print ("Your selection hasn't been recognise ")
                print('Please press "Y" to confirm',sel,'or "N" to cancel')
                confirm = input()
        continue
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
    global mylist
    mylist = ['1. For Espresso','2. For Double Espresso','3. For Americano','4. For Cappuccino']
    print("\n".join(mylist))
    # this part create an exception if the value is not INT
    #election = (input())
    Eccezione()

    print('Prima verifica passata con successo'
          )

####delete up to here
    global sel
    if selection == 1:
        sel = "Espresso"

    elif selection == 2:
        sel = "Double Espresso"

    elif selection == 3:
        sel = "Americano"

    elif selection == 4:
        sel = "Cappuccino"
    else:
        try:
            print('seconda eccezione')
            Eccezione()

            #global sel
        #### this part of the except is not working
        except ValueError:
            print('value error 2')
    print('You have selected', sel)


def Eccezione():
    global selection
    selection = (input())
    print('debug')
    while selection != mylist:
        if type(selection) == int:
            print('yes')
            continue
        else:
            try:
                selection = int(selection)
                print('conversione')
                #Eccezione()
                break
            except ValueError:
                print("Your selection hasn't been recognise ")
                print('Please make again your choose:')
                print("\n".join(mylist))
                selection = (input())
                print('eccezione value erro')
                continue