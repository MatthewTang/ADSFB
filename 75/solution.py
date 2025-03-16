import unittest
from typing import List, Optional


class Solution:
    # nums[i] is either 0, 1, or 2.
    def sortColors(self, nums: List[int]) -> None:
        counts = [0] * 3

        for n in nums:
            counts[n] += 1

        i = 0
        for j in range(len(counts)):
            for _ in range(counts[j]):
                nums[i] = j
                i += 1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [2, 0, 2, 1, 1, 0]
        s.sortColors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    # def test1(self):
    #     s = Solution()
    #     nums = [2, 0, 1]
    #     s.sortColors(nums)
    #     self.assertEqual(nums, [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
