from collections import deque
import unittest
from typing import Deque, List, Optional, Set, Tuple


# 33
class Solution:
    # def countPaths(self, grid: List[List[int]]) -> int:
    #     ROW, COL = len(grid), len(grid[0])
    #     directions = [
    #         (1, 0),
    #         (0, 1),
    #     ]
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

    def countPaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions: List[Tuple[int, int]] = [(1, 0), (0, 1)]

        q: Deque[Tuple[int, int]] = deque([(0, 0)])
        count = 0

        while q:
            curr = q.popleft()
            r, c = curr
            if r == ROW - 1 and c == COL - 1:
                count += 1
            for dr, dc in directions:
                _r, _c = r + dr, c + dc
                if _r < 0 or _c < 0:
                    continue
                if _r >= ROW or _c > COL:
                    continue
                q.append((_r, _c))

        return count


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [[0] * 4 for _ in range(4)]
        expected = 20
        result = s.countPaths(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
