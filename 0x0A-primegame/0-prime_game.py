#!/usr/bin/python3
""" A Module it is """


def isWinner(x, nums):
    """ A Function it is"""
    players = {
        "Maria": 0,
        "Ben": 0
    }
    highest = max(nums)
    primes = list(range(2, highest+1))
    sqrt = int((highest**0.5))
    for i in range(2, sqrt + 1):
        primes = list(filter(lambda x: ((x % i) != 0) or x == i, primes))

    for i in range(x):
        no = len(list(filter(lambda x: x <= nums[i], primes)))
        winner = "Ben" if (no % 2) == 0 else "Maria"
        players[winner] += 1

    if players["Maria"] < players["Ben"]:
        return "Ben"
    elif players["Maria"] == players["Ben"]:
        return None
    else:
        return "Maria"
