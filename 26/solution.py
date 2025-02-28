import unittest
from typing import List


# time complexity: O(n), space complexity: O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        _nums = []
        prev = None
        for i in range(len(nums)):
            curr = nums[i]
            if not curr == prev:
                count += 1
                _nums.append(curr)
                prev = curr

        nums[:] = _nums
        return count


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1, 1, 2]
        s = Solution()
        self.assertEqual(s.removeDuplicates(nums), 2)
        self.assertEqual(nums, [1, 2])

    def test2(self):
        nums = [0,0,1,1,1,2,2,3,3,4]
        s = Solution()
        self.assertEqual(s.removeDuplicates(nums), 5)
        self.assertEqual(nums, [0,1,2,3,4])


if __name__ == "__main__":
    unittest.main()
