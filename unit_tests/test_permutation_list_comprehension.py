import unittest
import sys
sys.path.append("D:/IT/Python/CodeSignal")
from assignments import permutation_list_comprehension

class Test(unittest.TestCase):
    
    def test_permutation(self):
        self.assertEqual(permutation_list_comprehension.permutation(1,1,1,2),[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]])
        self.assertEqual(permutation_list_comprehension.permutation(1,2,3,3),[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 3],
        [0, 2, 0], [0, 2, 2], [0, 2, 3], [1, 0, 0], [1, 0, 1], [1, 0, 3], [1, 1, 0], [1, 1, 2], [1, 1, 3], [1, 2, 1], [1, 2, 2], [1, 2, 3]])


if __name__ == "__main__":
    unittest.main()