'''
Is Substitution Cipher?

A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters.
For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.
A substitution cipher is a method of encoding where each letter of the plaintext alphabet is replaced with
the corresponding (i.e. having the same index) letter of some ciphertext alphabet.
Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) substitution ciphers.

For string1 = "aacb" and string2 = "aabc", the output should be isSubstitutionCipher(string1, string2) = true.
Any ciphertext alphabet that starts with acb... would make this transformation possible.
For string1 = "aa" and string2 = "bc", the output should be
isSubstitutionCipher(string1, string2) = false.
'''

def isSubstitutionCipher(string1, string2):
    return len(set(zip(string1, string2))) == len(set(string1)) == len(set(string2))

print(isSubstitutionCipher("aacb","aabc"))