import unittest
from typing import List, Optional


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return 2


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = 2
        result = s.uniquePathsWithObstacles(obstacleGrid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
