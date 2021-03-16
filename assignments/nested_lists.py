'''
Platform: HackerRank

Print the name(s) of any student(s) having the second lowest grade in.
If there are multiple students, order their names alphabetically and print each one on a new line.
'''

def second_lowest_grade():
    n = int(input())
    marksheet = dict([[input(), float(input())] for _ in range(n)])
    marksheet = dict(marksheet.items())
    minval = sorted(set(marksheet.values()))
    res = sorted([k for k, v in marksheet.items() if v == minval[1]])
    for x in res:
        print(x)

second_lowest_grade()