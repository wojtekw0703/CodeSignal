'''
Without using any string methods, try to print the following: 123...n
Example: n = 5
Print the string 12345.
'''
if __name__ == '__main__':
    n = int(input())
    result = []
    for i in range(1,n+1):
        result.append(str(i))
    tmp = ''.join(result)
    print(tmp)
