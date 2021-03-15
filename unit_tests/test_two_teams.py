import unittest
import sys
sys.path.append("D:/IT/Python/CodeSignal")
from assignments import two_teams

class TestTeams(unittest.TestCase):
    def test_teams(self):
        self.assertEqual(two_teams.twoTeams([1, 11, 13, 6, 14]), 11)
        self.assertEqual(two_teams.twoTeams([3, 4]), -1)
        self.assertEqual(two_teams.twoTeams([16, 14, 79, 8, 71, 72, 71, 10, 80, 76, 83, 70, 57, 29, 31]), 209)
        self.assertEqual(two_teams.twoTeams([23, 72, 54, 4, 88, 91, 8, 44]), -38)


if __name__ == "__main__":
    unittest.main()