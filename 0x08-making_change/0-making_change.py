#!/usr/bin/python3
""" alx python interview """


def makeChange(coins, total):
    """ Given a pile of coins of different values,
    determine the fewest number of coins needed to
    meet a given amount total
    """
    no = 0
    coins = sorted(coins, reverse=True)
    if total <= 0:
        return 0
    for coin in coins:
        print(coin)
        div = total//coin
        no += div
        total -= div * coin
        print(total)
        if total == 0:
            return no
    return -1
