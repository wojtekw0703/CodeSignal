import unittest
import sys
sys.path.append("D:/IT/Python/CodeSignal")
from assignments import get_commit

class TestCommit(unittest.TestCase):
    def test_commit(self):
        self.assertEqual(get_commit.getCommit("0??+0+!!someCommIdhsSt"),"someCommIdhsSt")
        self.assertEqual(get_commit.getCommit("noAUTHORofTHIScOmMiT"),"noAUTHORofTHIScOmMiT")
        self.assertEqual(get_commit.getCommit("?????!+0"),"")
        self.assertEqual(get_commit.getCommit("!0?!++?empThddsEldfeojLEJlfdk"),"empThddsEldfeojLEJlfdk")
        self.assertEqual(get_commit.getCommit("+?!00+?sdfejdcdfjwlejflsfjDjfejfLDJfodKJDFLJq"),"sdfejdcdfjwlejflsfjDjfejfLDJfodKJDFLJq")

if __name__ == "__main__":
    unittest.main()