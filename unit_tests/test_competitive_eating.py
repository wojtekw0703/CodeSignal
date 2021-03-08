import unittest
import sys
sys.path.append("D:/IT/Python/CodeSignal")
from assignments import competitive_eating

class TestCompetitive(unittest.TestCase):
    def test_competitive_eating(self):
        self.assertEqual(competitive_eating.competitiveEating(3.1415, 10, 2), "   3.14   ")
        self.assertEqual(competitive_eating.competitiveEating(29.8245, 10, 0), "    30    ")
        self.assertEqual(competitive_eating.competitiveEating(9.34, 4, 2), "9.34")
        self.assertEqual(competitive_eating.competitiveEating(837.28472, 20, 7), "    837.2847200     ")
        self.assertEqual(competitive_eating.competitiveEating(0, 4, 1), "0.0 ")
        self.assertEqual(competitive_eating.competitiveEating(666.2837, 15, 1), "     666.3     ")


if __name__ == "__main__":
    unittest.main()