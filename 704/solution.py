import unittest
from typing import List, Optional


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [-1, 0, 3, 5, 9, 12]
        result = s.search(nums, 9)
        self.assertEqual(result, 4)

    def test2(self):
        s = Solution()
        nums = [-1, 0, 3, 5, 9, 12]
        result = s.search(nums, 2)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
