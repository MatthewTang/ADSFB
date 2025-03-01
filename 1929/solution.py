import unittest
from typing import List


# time complexity: O(n), space complexity: O(n)
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(2 * len(nums)):
            a.append(nums[i % len(nums)])
        return a


class TestSolution(unittest.TestCase):
    def test1(self):
        nums = [1, 2, 1]
        s = Solution()
        self.assertEqual(s.getConcatenation(nums), [1, 2, 1, 1, 2, 1])

    def test2(self):
        nums = [1, 3, 2, 1]
        s = Solution()
        self.assertEqual(s.getConcatenation(nums), [1, 3, 2, 1, 1, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
