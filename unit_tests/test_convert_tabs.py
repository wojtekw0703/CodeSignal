import unittest
import sys
sys.path.append("D:/IT/Python/CodeSignal")
from assignments import convert_tabs

class TestConvert(unittest.TestCase):
    
    def test_convert(self):
        self.assertEqual(convert_tabs.convertTabs("\treturn False",4),"    return False")
        self.assertEqual(convert_tabs.convertTabs("",8),"")
        self.assertEqual(convert_tabs.convertTabs("    for x in range(20)",16),"    for x in range(20)")
        self.assertEqual(convert_tabs.convertTabs("\treturn\t",2),"  return  ")

if __name__ == "__main__":
    unittest.main()