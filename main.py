#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import *

# Write code for test
#
# All tests should be passed
    # write 'prime_check' function which input is a integer
    # and return True or False value
    # Értsd ellenőrízze, hogy az adott szám prim szám e

    # write 'square_number_check' function which input is a integer
    # and return True or False value

def main():

    return

def prime_check(number):
    result = True
    if number >= 3:
        for i in range(3, int(round(sqrt(number))) + 1):
            if number % i == 0:
                result = False
                break
    return result

def square_number_check(number):
    result = False
    if sqrt(number) == round(sqrt(number),0):
        result = True
    return result

if __name__ == '__main__':
    main()