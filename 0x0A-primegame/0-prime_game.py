#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a
prime number from the set and removing that number and its multiples
from the set. The player that cannot make a move loses the game.
They play x rounds of the game, where n may be different for each round.
Assuming Maria alwaysgoes first and both players play optimally,
determine who the winner of each game is.
"""


def isWinner(x, nums):
    """ Determining who the winner is """
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes = [i for i in range(n + 1) if primes[i]]
    m = 0
    for i in nums:
        m += sum(prime <= i for prime in primes)
    if m % 2 == 0:
        return "Ben"
    return "Maria"
