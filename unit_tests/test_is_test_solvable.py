import unittest
import sys

sys.path.append("D:/IT/Python/CodeSignal")
from assignments import is_test_solvable


class TestCommit(unittest.TestCase):
    def test_solvable(self):
        self.assertEqual(
            is_test_solvable.isTestSolvable([529665, 909767, 644200], 3), True
        )
        self.assertEqual(
            is_test_solvable.isTestSolvable(
                [
                    603040,
                    834416,
                    903427,
                    254312,
                    524329,
                    740203,
                    382224,
                    90673,
                    883043,
                    263478,
                    546458,
                    785567,
                ],
                7,
            ),
            True,
        )
        self.assertEqual(is_test_solvable.isTestSolvable([1010, 10], 4), False)
        self.assertEqual(is_test_solvable.isTestSolvable([1234, 56], 7), True)


if __name__ == "__main__":
    unittest.main()