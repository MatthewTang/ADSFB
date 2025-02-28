import unittest
from typing import List


# # time complexity: O(n^2)...
# class Solution:
#     # [1,2,3] -> [1,3]
#     # [1,2,3,4] -> [1,3,4]
#     def removeElementByIndex(self, nums: List[int], index: int) -> List[int]:
#         for i in range(index, len(nums)):
#             if i + 1 < len(nums):
#                 nums[i] = nums[i + 1]
#             else:
#                 nums[i] = None
# 
#     def removeElement(self, nums: List[int], val: int) -> int:
#         count = 0
#         i = 0
#         while i < len(nums):
#             print(nums)
#             if nums[i] == val:
#                 count += 1
#                 self.removeElementByIndex(nums, i)
#             else:
#                 i += 1
#         return len(nums) - count


# time complexity: O(n)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [3, 2, 2, 3]
        val = 3
        s = Solution()
        self.assertEqual(s.removeElement(nums, val), 2)
        self.assertEqual(nums[:2], [2, 2])

    def test2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        s = Solution()
        self.assertEqual(s.removeElement(nums, val), 5)
        self.assertEqual(nums[:5], [0, 1, 3, 0, 4])

    def test3(self):
        nums = [1]
        val = 1
        s = Solution()
        self.assertEqual(s.removeElement(nums, val), 0)
        self.assertEqual(nums[:0], [])


if __name__ == "__main__":
    unittest.main()
