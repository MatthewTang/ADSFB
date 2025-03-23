import unittest
from typing import List, Optional


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        res = []
        res.append([nums[0]])
        res.append([])

        for i in nums[1:]:
            tmp = []
            for j in res:
                l = j[:]
                l.append(i)
                tmp.append(l)
            res += tmp

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 2, 3]
        expected = [[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]
        result = s.subsets(nums)
        self.assertListEqual(sorted(result), sorted(expected))

    def test2(self):
        s = Solution()
        nums = [0]
        expected = [[], [0]]
        result = s.subsets(nums)
        self.assertListEqual(sorted(result), sorted(expected))

    def test3(self):
        s = Solution()
        nums = []
        expected = []
        result = s.subsets(nums)
        self.assertListEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
