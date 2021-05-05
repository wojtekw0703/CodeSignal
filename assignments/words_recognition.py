'''
Platform: CodeSignal

Given words word1 and word2, return an array of two strings sorted lexicographically,
where the first string contains characters present only in word1, and the second string
contains characters present only in word2.
'''

def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(set(w1) - set(w2)))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
