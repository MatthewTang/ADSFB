import unittest
from typing import List, Optional


# # hashmap
# class Solution:
#     # time: O(n), space: O(n)
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         countMap = {}
#         for n in nums:  # O(n)
#             if n in countMap:  # O(1)
#                 countMap[n] += 1  # O(1)
#             else:
#                 countMap[n] = 1  # O(1)
#
#         # O(n) + O(n)
#         return True in [count > 1 for count in countMap.values()]


# # hashmap optimal
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         countMap = {}
#         for n in nums:
#             if n in countMap:
#                 return True
#             else:
#                 countMap[n] = 1
#         return False


# hashset length
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 2, 3, 3]
        expected = True
        result = s.containsDuplicate(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [1, 2, 3, 4]
        expected = False
        result = s.containsDuplicate(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
