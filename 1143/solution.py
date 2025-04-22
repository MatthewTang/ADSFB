import unittest
from typing import List, Optional


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        text1 = "abcde"
        text2 = "ace"
        expected = 3
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
