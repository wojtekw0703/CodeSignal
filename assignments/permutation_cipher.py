'''
Platform: CodeSignal
Here's how permutation cipher works: the key to it consists of all the letters of the alphabet written up in some order.
All occurrences of letter 'a' in the encrypted text are substituted with the first letter of the key, all occurrences 
of letter 'b' are replaced with the second letter from the key, and so on, up to letter 'z' replaced with the last symbol of the key.

Given the password you always use, your task is to encrypt it using the permutation cipher with the given key.

For password = "iamthebest" and
key = "zabcdefghijklmnopqrstuvwxy", the output should be
permutationCipher(password, key) = "hzlsgdadrs"
'''

import string

def permutationCipher(password, key):
    # method to create a mapping table
    table = password.maketrans(string.ascii_lowercase,key)  # If a character is not specified in the dictionary/table, the character will not be replaced
    
    # returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table
    return password.translate(table) 
   
    

