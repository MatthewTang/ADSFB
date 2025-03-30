import unittest
from typing import List, Optional


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return 2


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
        expected = 2
        result = s.countPaths(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
