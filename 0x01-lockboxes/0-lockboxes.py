#!/usr/bin/python3
''' A module to check if a series of boxes containg
eachothers keys can all be opened
'''


def canUnlockAll(boxes):
    ''' Checks if a series of boxes containg eachothers keys
    can all be opened
    '''
    if len(boxes) <= 0:
        return True
    unlocked_boxes = set()
    unlocked_boxes.add(0)
    return check_unlocked_box(boxes[0], boxes, unlocked_boxes)


def check_unlocked_box(box, boxes, unlocked_boxes):
    ''' Helper function for canUnlockAll allows solution by
    Recursion
    '''
    for key in box:
        if key not in unlocked_boxes and key < len(boxes) and key >= 0:
            unlocked_boxes.add(key)
            check_unlocked_box(boxes[key], boxes, unlocked_boxes)
    if len(unlocked_boxes) == len(boxes):
        return True
    return False
