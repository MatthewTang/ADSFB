import unittest
from typing import List, Optional


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = currRow = [1] * n

        for _ in range(m - 1):
            for i in range(n - 2, -1, -1):
                currRow[i] = prevRow[i] + currRow[i + 1]
                prevRow = currRow

        return currRow[0]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        m = 3
        n = 7
        expected = 28
        result = s.uniquePaths(m, n)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        m = 3
        n = 2
        expected = 3
        result = s.uniquePaths(m, n)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        m = 2
        n = 1
        expected = 1
        result = s.uniquePaths(m, n)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
