#!/usr/bin/python3
"""
Function that calculates the min operations to copy and paste letters
"""


def minOperations(n): # 0-minoperations.py
    nOpe = 0 # operations counter - number of operations needed to result in exactly n H characters in this file.
    minOpe = 2 # minimum operations needed for a single operation (copy & paste) - for each pair
    while n > 1: # while n is greater than 1
        while n % minOpe == 0: # while n is divisible by minOpe, keep dividing it by minOpes
            nOpe += minOpe # increment the operations counter by minOpe - number of operations needed for a single operation (copy & paste) - for each pair
            n /= minOpe # divide n by minOpe
        minOpe += 1 # increment minOpe by 1
    return nOpe # return the operations counter - number of operations needed to result in exactly n H characters in this file.
