#!/usr/bin/python3
""" A Module it is """


def isWinner(x, nums):
    """ A Function it is """
    players = {
        "Maria": 0,
        "Ben": 0
    }
    i = 0
    while i < x:
        clist = list(range(1, nums[i]+1))
        player = None
        while True:
            player = "Ben" if player == "Maria" else "Maria"
            found = False
            for num in clist:
                if isPrime(num):
                    found = True
                    clist = removeMultiples(num, clist)
                    break
            if not found:
                winner = "Ben" if player == "Maria" else "Maria"
                players[winner] += 1
                break
        i += 1
        if players["Maria"] < players["Ben"]:
            return "Ben"
        elif players["Maria"] == players["Ben"]:
            return 
        else:
            return "Maria"


def isPrime(num):
    """ Another Function it is """
    if (num == 2):
        return True
    if ((num % 2) == 0 or num == 1):
        return False
    if (num == 3):
        return True
    for i in range(2, (num//2), 2):
        if not (((num % i)) == 0):
            return False
    return True


def removeMultiples(num, clist):
    """ Just another Fuction """
    multiples = []
    for i in clist:
        if (i % num) == 0:
            multiples.append(i)
    clist = list(filter(lambda x: x not in multiples, clist))
    return clist
