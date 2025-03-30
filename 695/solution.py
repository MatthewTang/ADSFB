import unittest
from typing import List, Optional


class Solution:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     row, col = len(grid), len(grid[0])
    #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    #
    #     def dfs(r, c):
    #         # out of bounds
    #         if r < 0 or c < 0 or r >= row or c >= col:
    #             return 0
    #         # sea
    #         if grid[r][c] == 0:
    #             return 0
    #
    #         grid[r][c] = 0
    #         area = 1
    #
    #         for dr, dc in directions:
    #             area += dfs(r + dr, c + dc)
    #
    #         return area
    #
    #     maxArea = 0
    #     for r in range(row):
    #         for c in range(col):
    #             if grid[r][c] == 1:
    #                 area = dfs(r, c)
    #                 maxArea = max(maxArea, area)
    #     return maxArea

    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    #     row, col = len(grid), len(grid[0])
    #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    #
    #     def dfs(r, c, count):
    #         # out of bounds
    #         if r < 0 or c < 0 or r >= row or c >= col:
    #             return
    #         # sea
    #         if grid[r][c] == 0:
    #             return
    #
    #         grid[r][c] = 0
    #         count[0] += 1
    #
    #         for dr, dc in directions:
    #             dfs(r + dr, c + dc, count)
    #
    #         return
    #
    #     maxCount = 0
    #     for r in range(row):
    #         for c in range(col):
    #             if grid[r][c] == 1:
    #                 count = [0]
    #                 dfs(r, c, count)
    #                 maxCount = max(maxCount, count[0])
    #     return maxCount
    #
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            # out of bounds
            if r < 0 or c < 0 or r >= row or c >= col:
                return 0
            # sea
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + sum([dfs(r + dr, c + dc) for dr, dc in directions])

        area = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area


class Test(unittest.TestCase):
    # def test1(self):
    #     s = Solution()
    #     grid = [
    #         [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    #         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    #     ]
    #     expected = 6
    #     result = s.maxAreaOfIsland(grid)
    #     self.assertIs(result, expected)
    #
    # def test2(self):
    #     s = Solution()
    #     grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    #     expected = 0
    #     result = s.maxAreaOfIsland(grid)
    #     self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        grid = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
        expected = 3
        result = s.maxAreaOfIsland(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
