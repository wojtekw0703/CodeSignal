"""
Platform: CodeSignal

You don't have time to investigate the problem, so you need to
implement a function that will fix the given array for you. Given result,
return an array of the same length, where the ith element is equal to the 
ith element of result with the last digit dropped.
"""


def fixResult(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))
