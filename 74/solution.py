import unittest
from typing import List, Optional


class Solution:
    # # time: O(logm + logn) -> O(log(m*n)), m no. of rows, n no. of cols, space: O(1)
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     rows, cols = len(matrix), len(matrix[0])
    #
    #     top, bot = 0, rows - 1
    #
    #     while top <= bot:
    #         row = (top + bot) // 2
    #         if target > matrix[row][-1]:
    #             top = row + 1
    #         elif target < matrix[row][0]:
    #             bot = row - 1
    #         else:
    #             break
    #
    #     if not (top <= bot):
    #         return False
    #
    #     l, r = 0, cols - 1
    #
    #     row = matrix[row]
    #
    #     while l <= r:
    #         m = (l + r) // 2
    #         if row[m] > target:
    #             r = m - 1
    #         elif row[m] < target:
    #             l = m + 1
    #         else:
    #             return True
    #
    #     return False

    # time: O(log(m*n)), space: O(1), m no. of rows, n no. of cols, single loop approach
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            m = (l + r) // 2
            row, col = m // cols, m % cols
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True

        return False


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        result = s.searchMatrix(matrix, 3)
        self.assertTrue(result)

    def test2(self):
        s = Solution()
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
        result = s.searchMatrix(matrix, 13)
        self.assertFalse(result)

    def test3(self):
        s = Solution()
        matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
        result = s.searchMatrix(matrix, 11)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
