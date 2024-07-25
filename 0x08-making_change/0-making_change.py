#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    change = 0
    for c in coins:
        if total <= 0:
            break
        change += total // c
        total = total % c
    if total != 0:
        return -1
    return change
