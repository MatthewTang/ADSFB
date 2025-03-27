import unittest
from typing import List, Optional


# class Solution:
#     # time: O(n^2), space: O(n)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         countMap = {}
#         for i in range(len(nums)):  # O(n)
#             n = nums[i]  # O(1)
#             for c in countMap:  # O(n)
#                 if c + n == target:  # O(1)
#                     return [countMap[c], i]  # O(1)
#
#             countMap[n] = i  # O(1)


class Solution:
    # O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countMap = {}
        for i, n in enumerate(nums):  # O(n)
            diff = target - n  # O(1)
            if diff in countMap:  # O(1)
                return [countMap[diff], i]

            countMap[n] = i  # O(1)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = s.twoSum(nums, target)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = s.twoSum(nums, target)
        self.assertListEqual(result, expected)

    def test3(self):
        s = Solution()
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = s.twoSum(nums, target)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
