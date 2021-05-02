"""
Platform: CodeSignal

Given the names of the companies, return the list of characters
that are popular but not mainstream sorted by their ASCII codes.
"""


def startupName(companies):
    comp1 = set(companies[0])
    comp2 = set(companies[1])
    comp3 = set(companies[2])
    res = ((comp1 & comp2) | (comp2 & comp3) | (comp1 & comp3)) - (
        comp1 & comp2 & comp3
    )
    return list(sorted(list(res)))


print(startupName(["coolcompany", "nicecompany", "legendarycompany"]))