'''
Platform: Code Signal
Implement a function that, given a piece of code and a positive integer x 
will turn each tabulation character in code into x whitespace characters.

For code = "\treturn False" and x = 4, the output should be
convertTabs(code, x) = "    return False"
'''

def convertTabs(code, x):
    return code.replace('\t'," "*x)


# print(convertTabs("\treturn False",4))

