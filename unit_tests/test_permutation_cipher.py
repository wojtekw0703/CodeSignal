import unittest
import sys
sys.path.append("D:/IT/Python/CodeSignal")
from assignments import permutation_cipher

class Test(unittest.TestCase):
    def test_permutation(self):
        self.assertEqual(permutation_cipher.permutationCipher("iamthebest", "zabcdefghijklmnopqrstuvwxy"), "hzlsgdadrs")
        self.assertEqual(permutation_cipher.permutationCipher("codesignalrocks", "ebtyfkudagizxmvcnojqwlsrhp"),"tvyfjaumezovtij")
        self.assertEqual(permutation_cipher.permutationCipher("supersecurepassword", "felkjmwchynzgobvadtipqrxsu"),"tpvjdtjlpdjvfttrbdk")
        self.assertEqual(permutation_cipher.permutationCipher("myprivatestuff", "mvdwjsphaqufinryoltxcgkzbe"),"ibylagmxjtxcss")


if __name__ == "__main__":
    unittest.main()