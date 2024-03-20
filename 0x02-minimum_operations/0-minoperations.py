#!/usr/bin/python3
"""
Function that calculates the min operations to copy and paste letters
"""


def minOperations(n): # 0-minoperations.py
    nOpe = 0 # number of operations
    minOpe = 2 # minimum operation needed for each pair
    while n > 1: # while n is greater than 1, keep going until it's not
        while n % minOpe == 0: # while n is divisible by minOpe
            nOpe += minOpe # increment nOpe by minOpe 
            n /= minOpe # divide n by minOpe
        minOpe += 1 # increment minOpe by 1
    return nOpe # return nOpe which will be equal to the number of pairs minus 1
