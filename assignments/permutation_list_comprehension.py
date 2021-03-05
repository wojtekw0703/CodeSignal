'''
Platform: HackerRank

You are given three integers  and  representing the dimensions of a cuboid along with an integer.
Print a list of all possible coordinates given by on a 3D grid where the sum of x,y,z is not equal to n 
'''
def permutation(x,y,z,n):
    res = [[v,b,n] for v in range(x+1)
               for b in range(y+1)
               for n in range(z+1)]
    
    return [x for x in res if sum(x) != n]