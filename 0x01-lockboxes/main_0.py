#!/usr/bin/python3

canUnlockAll = __import__('tmp2').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = [[10, -3, 1], [3]]
print(canUnlockAll(boxes))

boxes = [[None, None], []]
print(canUnlockAll(boxes))
