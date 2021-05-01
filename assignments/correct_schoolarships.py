"""
Platform: CodeSignal

You are given lists of unique student ids bestStudents, scholarships and allStudents,
representing ids of the best students, students that will get a scholarship and all the students
in the university, respectively. Return true if the scholarships are correctly distributed and false otherwise.
"""


def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)


print(correctScholarships([3, 5], [3, 5, 7], [1, 2, 3, 4, 5, 6, 7]))
