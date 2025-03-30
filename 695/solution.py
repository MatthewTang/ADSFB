import unittest
from typing import List, Optional


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        return 6


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
        expected = 6
        result = s.maxAreaOfIsland(grid)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
        expected = 0
        result = s.maxAreaOfIsland(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
