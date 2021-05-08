"""
Platform: CodeSignal

Given a list of digits as they are written in the clockwise order,
find all other combinations the password could possibly have.
"""

from collections import deque


def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda d: res[d].rotate(-d), range(n)), 0)
    return [list(d) for d in res]


print(doodledPassword([1, 2, 3, 4, 5]))