#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    """
    n = len(boxes)
    if n == 0:
        return False

    visited = set()
    keys = set(boxes[0])

    visited.add(0)  # The first box is always unlocked

    while keys:
        box_key = keys.pop()
        if box_key not in visited and 0 <= box_key < n:
            visited.add(box_key)
            keys.update(boxes[box_key])

    return len(visited) == n
