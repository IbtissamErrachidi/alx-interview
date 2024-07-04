#!/usr/bin/python3
"""
involves determining.
"""


def canUnlockAll(boxes):
    n = len(boxes)
    opens = set()
    keys = [0]

    while keys:
        key = keys.pop()
        if key not in opens:
            opens.add(key)
            for new_key in boxes[key]:
                if new_key < n:
                    keys.append(new_key)
    
    return len(opens) == n
