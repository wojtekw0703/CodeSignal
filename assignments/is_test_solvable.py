"""
Platform: CodeSignal

Given the list of question ids, determine if the sum of their
digits is divisible by k to see if it's worth trying to pass the test.
"""


def isTestSolvable(ids, k):
    digitSum = lambda fun: sum(int(digit) for digit in str(fun))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0


print(isTestSolvable([529665, 909767, 644200], 3))
