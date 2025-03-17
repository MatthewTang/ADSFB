import unittest
from typing import List, Optional


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1

    def binarySearchRange(self, low: int, high: int) -> int:
        while low <= high:
            mid = (low + high) // 2
            if self.isCorrect(mid) > 0:
                high = mid - 1
            elif self.isCorrect(mid) < 0:
                low = mid + 1
            else:
                return mid
        return -1

    def isCorrect(self, n: int) -> int:
        if n > 10:
            return 1
        elif n < 10:
            return -1
        else:
            return 0


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.binarySearch([1, 2, 3, 4, 5], 3), 2)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.binarySearchRange(0, 20), 10)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.isCorrect(10), 0)

    def test4(self):
        sol = Solution()
        self.assertEqual(sol.binarySearchRange(0, 9), -1)


if __name__ == "__main__":
    unittest.main()
