'''
Platform: CodeSignal

The track of time will be kept by a float number. It will be displayed 
on the board with the set precision precision with center alignment, and it is
guaranteed that it will fit in the screen. Your task is to test the billboard.
Given the time t, the width of the screen and the precision with which the time should be displayed, 
return a string that should be shown on the billboard.

For t = 3.1415, width = 10, and precision = 2,
the output should be "   3.14   "
'''

def competitiveEating(t, width, precision):
    return "{0:.{1}f}".format(t,precision).center(width)


