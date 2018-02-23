import unittest

class unitest(unittest.TestCase):
    def testEmptyString(self):
        Input = ""
        Output = ""
        self.assertEqual(Solution().reverseString(Input),Output)
    def testSampleString(self):
        Input = "hello"
        Output = "olleh"
        self.assertEqual(Solution().reverseString(Input),Output)

class Solution():
    def reverseString(self, s):
        return s[::-1]

if __name__ == '__main__':
    unittest.main()
