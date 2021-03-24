'''
Platform: HackerRank

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
'''

if __name__ == '__main__':
    n = int(input())  # input a number and convert to integer 
    student_marks = {} # declaring a dict 
    for _ in range(n): 
        name, *line = input().split() # splitting the line into name and numbers
        scores = list(map(float, line)) #mapping line into float scores and then create a list of them
        student_marks[name] = scores #assigning a value to certain student
    query_name = input()
    sum_marks = sum(student_marks[query_name]) # sum all values and assign to result variable
    print("{:.2f}".format(sum_marks/(len(scores)))) # print format