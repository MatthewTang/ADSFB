import unittest
from typing import List, Optional


class Solution:
    def hammingWeight(self, n):
        c = 0
        while n:
            c += 1 if n & 1 else 0
            n >>= 1
        return c


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 11
        expected = 3
        result = s.hammingWeight(n)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        n = 128
        expected = 1
        result = s.hammingWeight(n)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        n = 2147483645
        expected = 30
        result = s.hammingWeight(n)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
