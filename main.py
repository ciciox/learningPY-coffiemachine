from selection import Main

import payment
import time

Main()
time.sleep(2)
print ('Your coffie now is Ready')

print ('Your remaining credit is',payment.credit -1)
time.sleep(1)
print('Please collect your change and enjoy your drink')
credit = 0

##create a for to print multiple line  or clearscreen for all platform

print('')
print('')
print('')

# restart app
Main()
