"""
Platform: CodeSignal

Given a list of courses, remove the courses with titles consisting of
x letters and return the result.
"""


def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))
