import unittest
from typing import List, Optional, Set, Tuple


class Solution:
    # time complexity: O(4^(m*n)), space complexity: O(m*n), where m is the number of rows and n is the number of columns
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int, visit: Set[Tuple[int, int]]) -> int:
            row, col = len(grid), len(grid[0])

            # visited
            if (r, c) in visit:
                return 0
            # out of bounds
            if r < 0 or c < 0 or r >= row or c >= col:
                return 0
            # into wall
            if grid[r][c] == 1:
                return 0
            # reach bottom right
            if r == row - 1 and c == col - 1:
                return 1

            count = 0
            visit.add((r, c))
            count += dfs(r - 1, c, visit)
            count += dfs(r, c + 1, visit)
            count += dfs(r + 1, c, visit)
            count += dfs(r, c - 1, visit)
            visit.remove((r, c))

            return count

        return dfs(0, 0, set())


# class Solution:
#     def countPaths(self, grid: List[List[int]]) -> int:
#         def dfs(r: int, c: int, visit: List[List[int]]) -> int:
#             row, col = len(grid), len(grid[0])
#
#             # out of bounds
#             if r < 0 or c < 0 or r >= row or c >= col:
#                 return 0
#             # into wall
#             if grid[r][c] == 1:
#                 return 0
#             # visited
#             if visit[r][c]:
#                 return 0
#             # reach bottom right
#             if r == row - 1 and c == col - 1:
#                 return 1
#
#             count = 0
#             visit[r][c] = True
#             count += dfs(r - 1, c, visit)
#             count += dfs(r, c + 1, visit)
#             count += dfs(r + 1, c, visit)
#             count += dfs(r, c - 1, visit)
#             visit[r][c] = False
#
#             return count
#
#         return dfs(0, 0, [[False] * len(grid[0]) for _ in range(len(grid))])


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
        expected = 2
        result = s.countPaths(grid)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        grid = [[0, 0, 0, 0]]
        expected = 1
        result = s.countPaths(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
