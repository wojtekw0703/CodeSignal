'''
Platform: CodeSignal

Given the list of task ids in your toDo list, remove each kth 
task from it and return the list of remaining tasks.
'''

def removeTasks(k, toDo):
    del toDo[k-1::k]
    return toDo
