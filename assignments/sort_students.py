"""
Platform: CodeSignal

Your task is to sort the students lexicographically
by their surnames. If two students happen to have the same surname,
their order in the result should be the same as in the original list.
"""


def sortStudents(students):
    students.sort(key=lambda student: student.split(" ")[-1])
    return students
