'''
Platform: HackerRank

You are given a NxM integer array matrix with space separated elements (N = rows and M = columns).
Your task is to print the transpose and flatten results.
'''
import numpy

n,m=map(int,input().split())
lista=[list(map(int,input().split())) for i in range(n)]

a=numpy.array(lista)
print(numpy.transpose(a))
print(a.flatten())