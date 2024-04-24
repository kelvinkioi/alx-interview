#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Given a number n, write a method that calculates the fewest
    number of operations needed to result in exactly n H
    characters in the file.
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0

    result = 0
    i = 2
    while i <= n:
        if n % i == 0:
            result += i
            n /= i
            i -= 1
        i += 1
    return int(result)
