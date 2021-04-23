"""
Platform: CodeSignal
To begin with, you need to construct a
multiplication table. Given an integer n, return the multiplication table of size n × n.
"""


def multiplicationTable(n):
    return [[x * y for x in range(1, n + 1)] for y in range(1, n + 1)]
