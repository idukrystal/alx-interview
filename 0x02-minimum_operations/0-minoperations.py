#!/usr/bin/env python3
'''
In a text file, there is a single character H. Your text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters
in the file
'''


def minOperations(n: int) -> int:
    '''
     (A) do this until we have n (h)'s in file:
        (1) copy value in file to clipboard
        (2) continue to paste value in clipboard to file
            until the total can perfectly divide (n)
        (3) go back to step (1)

    (B) returns the number of copy/paste performed
    '''
    copy = 0  # No of times file content is copied to clipboard
    paste = 0  # No of times clipboard content is pasted in file
    _file = 1  # No of (H)'s in file
    clipboard = 0  # No of (H)'s in clipboard

    while _file < n:  # while no of (H)'s in file < n

        # If no of (H)'s in file\ can divide "n""
        # or clipboard is empty (i.e in first time around)
        if clipboard == 0 or n % _file == 0:
            #  Copy file content to clipboard
            clipboard = _file
            copy += 1

        #  Paste cliboard content into file
        _file += clipboard
        paste += 1

    return copy + paste  # No of operations = copies + pastes
