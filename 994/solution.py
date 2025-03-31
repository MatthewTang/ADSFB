import unittest
from typing import List, Optional
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        time, fresh = 0, 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        if fresh == 0:
            return 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if new_r < 0 or new_c < 0 or new_r >= ROW or new_c >= COL:
                        continue

                    if grid[new_r][new_c] == 0:
                        continue

                    if grid[new_r][new_c] == 2:
                        continue

                    grid[new_r][new_c] = 2
                    fresh -= 1
                    queue.append((new_r, new_c))

            time += 1

        return time - 1 if fresh == 0 else -1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
        expected = 4
        result = s.orangesRotting(grid)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
        expected = -1
        result = s.orangesRotting(grid)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        grid = [[0, 2]]
        expected = 0
        result = s.orangesRotting(grid)
        self.assertIs(result, expected)

    def test4(self):
        s = Solution()
        grid = [[2, 2, 1], [1, 1, 0], [0, 1, 1]]
        expected = 3
        result = s.orangesRotting(grid)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        grid = [[0]]
        expected = 0
        result = s.orangesRotting(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
