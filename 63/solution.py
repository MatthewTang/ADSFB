import unittest
from typing import List, Optional
from functools import lru_cache


class Solution:
    # # dfs, time: O(2^(m+n)), space(m+n)
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #
    #     def dfs(r, c):
    #         if r >= m or c >= n:
    #             return 0
    #
    #         if obstacleGrid[r][c] == 1:
    #             return 0
    #
    #         if r == m - 1 and c == n - 1:
    #             return 1
    #
    #         return dfs(r + 1, c) + dfs(r, c + 1)
    #
    #     return dfs(0, 0)

    # # dfs w cache: O(m*n), space(m*n)
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #
    #     cache = [[0] * n for _ in range(m)]
    #     def dfs(r, c):
    #         if r >= m or c >= n:
    #             return 0
    #
    #         if obstacleGrid[r][c] == 1:
    #             return 0
    #
    #         if cache[r][c]:
    #             return cache[r][c]
    #
    #         if r == m - 1 and c == n - 1:
    #             cache[r][c] = 1
    #
    #         else:
    #             cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
    #
    #         return cache[r][c]
    #
    #     return dfs(0, 0)

    # bottom-up dp: time: O(m*n), space: O(n)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n

        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif i == 0:
                    dp[j] = dp[j - 1]
                elif j == 0:
                    dp[j] = dp[j]
                else:
                    dp[j] = dp[j] + dp[j - 1]

        return dp[-1]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        expected = 2
        result = s.uniquePathsWithObstacles(obstacleGrid)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        obstacleGrid = [[0, 0], [0, 1]]
        expected = 0
        result = s.uniquePathsWithObstacles(obstacleGrid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
