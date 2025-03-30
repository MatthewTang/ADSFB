import unittest
from typing import List, Optional, Set


class Solution:
    # time: O(m*n), space: O(m*n)
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        def dfs(r, c, visited: Set) -> None:
            # out of bounds
            if r < 0 or c < 0 or r >= row or c >= col:
                return
            # sea
            if grid[r][c] == "0":
                return
            # visited
            if (r, c) in visited:
                return

            visited.add((r, c))

            dfs(r - 1, c, visited)
            dfs(r, c + 1, visited)
            dfs(r + 1, c, visited)
            dfs(r, c - 1, visited)

        visited = set()
        islands = 0

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "0":
                    continue
                if (r, c) in visited:
                    continue

                dfs(r, c, visited)
                islands += 1

        return islands


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

    def test3(self):
        s = Solution()
        grid = [
            ["1", "0"],
            ["0", "1"],
        ]
        expected = 2
        result = s.numIslands(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
