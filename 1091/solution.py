import unittest
from typing import Deque, List, Optional
from collections import deque


class Solution:
    # time: O(m*n), space: O(m*n)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1

        ROW, COL = len(grid), len(grid[0])
        directions = [
            (-1, 0),  # up
            (-1, 1),  # up-right
            (0, 1),  # right
            (1, 1),  # down-right
            (1, 0),  # down
            (1, -1),  # down-left
            (0, -1),  # left
            (-1, -1),  # up-left
        ]
        q = deque([(0, 0)])
        visit = {(0, 0)}
        length = 1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROW - 1 and c == COL - 1:
                    # print(r, c, length)
                    return length

                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if new_r < 0 or new_c < 0 or new_r >= ROW or new_c >= COL:
                        continue
                    if grid[new_r][new_c] == 1:
                        continue
                    if (new_r, new_c) in visit:
                        continue
                    visit.add((new_r, new_c))
                    q.append((new_r, new_c))
            # print(r, c, length)
            length += 1

        return -1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        grid = [[0, 1], [1, 0]]
        expected = 2
        result = s.shortestPathBinaryMatrix(grid)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        expected = 4
        result = s.shortestPathBinaryMatrix(grid)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
        expected = -1
        result = s.shortestPathBinaryMatrix(grid)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
