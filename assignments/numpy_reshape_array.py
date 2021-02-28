import numpy
'''
Platform: HackerRank
You are given a space separated list of nine integers. Your task is to convert this list into a 3x3 NumPy array.
'''

a=numpy.array(list(map(int,input().split())))
print(numpy.reshape(a,(3,3)))