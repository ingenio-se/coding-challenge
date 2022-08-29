from app import analyze
import unittest

class TestAnalyze(unittest.TestCase):
    def test_1(self):
        pairs = analyze('1,9,5,0,20,-4,12,16,7',12)
        self.assertEqual(pairs, ["5,7","0,12","-4,16"])

    def test_2(self):
        pairs = analyze('1,9,5,0,20,-4,12,16,7',10)
        self.assertEqual(pairs, ["1,9"])
    
    def test_3(self):
        pairs = analyze('1,9,5,0,20,-4,12,16,7',100)
        self.assertEqual(pairs, [])

    def test_4(self):
        pairs = analyze('1,2,3,4,5,6,7,8,9',10)
        self.assertEqual(pairs, ["1,9","2,8","3,7","4,6"])

    def test_5(self):
        pairs = analyze('1,2,3,4,5,6,7,8,9',6)
        self.assertEqual(pairs, ["1,5","2,4"])

if __name__ == '__main__':
    unittest.main()