import time
from selection import
print('Welcome please select your choice')
#time.sleep(1)
print('Press:')
#time.sleep(1)
print('1. For Espresso')
print('2. For Double Espresso')
print('3. For Americano')
print('4. For Cappuccino')
#### restart point

'''
this part works but will be migrate to became a function '''
'''

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
'''

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

