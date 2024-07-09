#!/usr/bin/python3
"""
calculates the fewest number of operations needed .
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed .
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
