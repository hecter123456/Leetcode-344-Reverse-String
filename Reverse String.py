import unittest

class unitest(unittest.TestCase):
    def testEmptyString(self):
        Input = ""
        Output = ""
        self.assertEqual(Solution().reverseString(Input),Output)

class Solution():
    def reverseString(self, s):
        if s == "":
            return ""

if __name__ == '__main__':
    unittest.main()
