"""
Platform: CodeSignal

A 2D list lst of size 2 * n - 1 is called a shell if it is filled with zeros and has the following configuration:

lst[0] contains one element;
lst[1] contains two elements;
...
lst[n - 2] contains n - 1 elements;
lst[n - 1] contains n elements;
...

"""


def constructShell(n):
    return [[0] * (n - abs(i)) for i in range(-n + 1, n)]
