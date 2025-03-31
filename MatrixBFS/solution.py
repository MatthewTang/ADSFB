import unittest
from typing import List, Optional, Deque, Set, Tuple
from collections import deque


class Solution:
    # time: O(m*n), space: O(m*n)
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue: Deque[Tuple[int, int]] = deque([(0, 0)])
        visit: Set[Tuple[int, int]] = {(0, 0)}
        length = 0

        if not grid or grid[0][0] == 1:
            return -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == ROW - 1 and c == COL - 1:
                    return length

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    # out of bounds
                    if new_r < 0 or new_c < 0 or new_r >= ROW or new_c >= COL:
                        continue

                    # wall
                    if grid[new_r][new_c] == 1:
                        continue

                    # visited
                    if (new_r, new_c) in visit:
                        continue

                    queue.append((new_r, new_c))
                    visit.add((new_r, new_c))
            length += 1

        return -1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
        expected = 6
        result = s.shortestPath(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
