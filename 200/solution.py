import unittest
from typing import List, Optional


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        return 0


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        expected = 1
        result = s.numIslands(grid)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        expected = 3
        result = s.numIslands(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
