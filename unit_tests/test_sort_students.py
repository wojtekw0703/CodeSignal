import unittest
from unittest.mock import patch
import sys

sys.path.append("D:/IT/Python/CodeSignal")
from assignments import sort_students


class TestNestedLists(unittest.TestCase):
    def test_sort(self):
        self.assertEqual(
            sort_students.sortStudents(
                ["John Smith", "Jacky Mon Simonoff", "Lucy Smith", "Angela Zimonova"]
            ),
            ["Jacky Mon Simonoff", "John Smith", "Lucy Smith", "Angela Zimonova"],
        )
        self.assertEqual(sort_students.sortStudents(["Kate"]), ["Kate"])
        self.assertEqual(
            sort_students.sortStudents(["John Doe", "Brick Tick", "Batman"]),
            ["Batman", "John Doe", "Brick Tick"],
        )


if __name__ == "__main__":
    unittest.main()