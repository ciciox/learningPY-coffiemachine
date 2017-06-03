__author__ = 'Giuseppe Faro'
from core import *


def Workflow():

    Selection()
    Confirmation()
    Clearscreen()


def Clearscreen():
    ## Sys Clear Screen function
    import platform
    import os
    op = platform.system()

    if op == ('Windows'):
        os.system('cls')
    elif op == Linux:
        os.system('clear')
    else:
        print("\n" * 70)


# Start Application
while Workflow() != 0:
    Workflow()