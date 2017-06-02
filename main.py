__author__ = 'Giuseppe Faro'

from selection import *
import payment
import time

Main()
time.sleep(2)
print ('Your coffie now is Ready')

print ('Your remaining credit is',payment.credit -1)
time.sleep(1)
print('Please collect your change and enjoy your drink')
time.sleep(4)
credit = 0


## Clear Screen part

import platform
import os
op = platform.system()

if op == ('Windows'):
    os.system('cls')
elif op == Linux:
    os.system('clear')
else:
    print("\n" * 70)

# Restart app
Main()

