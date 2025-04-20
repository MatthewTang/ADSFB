from collections import deque
import unittest
from typing import Deque, List, Optional, Set, Tuple


# 33
class Solution:
    # # time: O(2^(m*n))
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     ROW, COL = len(grid), len(grid[0])
    #     directions = [(1, 0), (0, 1)]
    #
    #     def dfs(r: int, c: int, visited: Set[Tuple[int, int]]):
    #         if r == ROW - 1 and c == COL - 1:
    #             return 1
    #
    #         if r < 0 or c < 0:
    #             return 0
    #
    #         if r >= ROW or c >= COL:
    #             return 0
    #
    #         if (r, c) in visited:
    #             return 0
    #
    #         visited.add((r, c))
    #         count = 0
    #         for dr, dc in directions:
    #             count += dfs(r + dr, c + dc, visited)
    #         visited.remove((r, c))
    #
    #         return count
    #
    #     return dfs(0, 0, set())

    # optimised, time: O(2^(m*n))
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            if r == ROW - 1 and c == COL - 1:
                return 1

            if r >= ROW or c >= COL:
                return 0

            return dfs(r + 1, c) + dfs(r, c + 1)

        return dfs(0, 0)

    # def countPaths(self, grid: List[List[int]]) -> int:
    #     ROW, COL = len(grid), len(grid[0])
    #     directions: List[Tuple[int, int]] = [(1, 0), (0, 1)]
    #
    #     q: Deque[Tuple[int, int]] = deque([(0, 0)])
    #     count = 0
    #
    #     while q:
    #         curr = q.popleft()
    #         r, c = curr
    #         if r == ROW - 1 and c == COL - 1:
    #             count += 1
    #         for dr, dc in directions:
    #             _r, _c = r + dr, c + dc
    #             if _r < 0 or _c < 0:
    #                 continue
    #             if _r >= ROW or _c > COL:
    #                 continue
    #             q.append((_r, _c))
    #
    #     return count
    #
    # # memoisation, time: O(m*n)
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     ROW, COL = len(grid), len(grid[0])
    #     directions = [(1, 0), (0, 1)]
    #     cache = [[0] * COL for _ in range(ROW)]
    #
    #     def dfs(r: int, c: int, visited: Set[Tuple[int, int]]):
    #         if r < 0 or c < 0:
    #             return 0
    #
    #         if r >= ROW or c >= COL:
    #             return 0
    #
    #         if (r, c) in visited:
    #             return 0
    #
    #         if cache[r][c]:
    #             return cache[r][c]
    #
    #         if r == ROW - 1 and c == COL - 1:
    #             cache[r][c] = 1
    #             return 1
    #
    #         visited.add((r, c))
    #         count = 0
    #         for dr, dc in directions:
    #             count += dfs(r + dr, c + dc, visited)
    #         visited.remove((r, c))
    #
    #         cache[r][c] = count
    #
    #         return count
    #
    #     return dfs(0, 0, set())

    # # optimised, memoised, time: O(2^(m*n))
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     ROW, COL = len(grid), len(grid[0])
    #     cache = [[0] * COL for _ in range(ROW)]
    #
    #     def dfs(r: int, c: int):
    #         if r >= ROW or c >= COL:
    #             return 0
    #
    #         if cache[r][c]:
    #             return cache[r][c]
    #
    #         if r == ROW - 1 and c == COL - 1:
    #             cache[r][c] = 1
    #         else:
    #             cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
    #
    #         return cache[r][c]
    #
    #     return dfs(0, 0)

    # bottom-up dp
    def countPaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dp = [1] * (COL - 1)
        for _ in range(ROW-1):
            for i in range(len(dp)):
                dp[i] = dp[i] + dp[i-1] if i > 0 else dp[i] + 1

        return dp[-1]


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [[0] * 4 for _ in range(4)]
        expected = 20
        result = s.countPaths(grid)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        grid = [[0] * 3 for _ in range(3)]
        expected = 6 
        result = s.countPaths(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
