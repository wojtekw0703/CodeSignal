"""
Platform: CodeSignal

To confirm your theory, you'd like to create a histogram showing
the number of assignments he completed each day in the given period. 
Given this assignments, return a list representing a horizontal histogram, 
where each bar is formed by the given character ch.
"""


def createHistogram(ch, assignments):
    return [ch * n for n in assignments]


print(createHistogram("*", [12, 12, 14, 3, 12, 15, 14]))
