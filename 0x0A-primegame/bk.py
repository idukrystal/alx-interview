#!/usr/bin/python3
""" A Module it is """



def isWinner(x, nums):
    """ A Function it is"""
    if (x > 90):
        pass#print(str(nums))
    players = {
        "Maria": 0,
        "Ben": 0
    }
    highest = max(nums);
    primes = list(range(2, highest));
    sqrt = 0;
    while (sqrt * sqrt) < highest:
        sqrt += 1

    print(sqrt)
    for i in range(2, sqrt):
        #if isPrime(i):
        print(i)
        primes = list(filter(lambda x: ((x % i) != 0) or x == i , primes))
    i = 0
    while i < x:
        clist = list(range(1, nums[i]+1))
        player = None
        while True:
            player = "Ben" if player == "Maria" else "Maria"
            found = False
            for num in clist:
                if num in primes:
                    found = True
                    clist = list(filter(lambda x: (x % num) != 0,clist));
                    break
            if not found:
                winner = "Ben" if player == "Maria" else "Maria"
                print(f' {i}  >>> {winner}')
                players[winner] += 1
                break
        i += 1
    if players["Maria"] < players["Ben"]:
        return "Ben"
    elif players["Maria"] == players["Ben"]:
        return None
    else:
        return "Maria"


def isPrime(num):
    """ Another Function it is """
    if (num == 2):
        return True
    if ((num % 2) == 0 or num == 1 or num == 0):
        return False
    if (num == 3):
        return True
    for i in range(3, (num//2), 2):
        if ((num % i) == 0):
            return False
    return True




print(isWinner(10000, list(range(10000))))
