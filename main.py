import time
print('Welcome please select your choice')
#time.sleep(1)
print('Press:')
#time.sleep(1)
print('1. For Espresso')
print('2. For Double Espresso')
print('3. For Americano')
print('4. For Cappuccino')
#### restart point

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
# restart point

if confirm == ('y'):
        #or 'Y':
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

'''


if selection == 1:
    print('You have selected "Espresso"')
    print('Please press "Y" to confirm')
    confirm = input()
    if confirm == y or Y:
        print('Your coffie will be ready shortly ')
        time.sleep(2)
    else:
       print ("Your selection hasn't been recognise ")
        #### restart from the second IF

elif selection == 2:
    print('You have selected "Double Espresso"')
    print('Please press "Y" to confirm')
    ##
    print('Please press "Y" to confirm')

else:
    print ("Your selection hasn't been recognise ")
    print('Please make again your choose')
    '''
'''
elif selection = 2:

elif selection = 3:

else selection = 4:
'''

