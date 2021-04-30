"""
Platform: CodeSignal

Given a document, return an array of all unique characters
that appear in it sorted by their ASCII codes.
"""


def uniqueCharacters(document):
    return sorted(set(list(document)))


print(uniqueCharacters("Todd told Tom to trot to the timber"))