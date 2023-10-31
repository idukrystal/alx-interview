#!/usr/bin/python3
""" A Module it is """


def isWinner(x, nums):
    """ A Function it is"""
    players = {
        "Maria": 0,
        "Ben": 0
    }
    highest = max(nums)
    primes = list(range(2, highest))
    sqrt = 0
    while (sqrt * sqrt) < highest:
        sqrt += 1
    for i in range(2, sqrt):
        primes = list(filter(lambda x: ((x % i) != 0) or x == i, primes))
    i = 0
    while i < x:
        no = len(list(filter(lambda x: x <= nums[i], primes)))
        winner = "Ben" if (no % 2) == 0 else "Maria"
        players[winner] += 1
        i += 1

    if players["Maria"] < players["Ben"]:
        return "Ben"
    elif players["Maria"] == players["Ben"]:
        return None
    else:
        return "Maria"
