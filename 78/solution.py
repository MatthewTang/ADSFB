import unittest
from typing import List, Optional


class Solution:
    # # time: O(n*(2^n))
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 0:
    #         return [[]]
    #
    #     res = []
    #     res.append([nums[0]])
    #     res.append([])
    #
    #     for i in nums[1:]: # O(n)
    #         tmp = []
    #         for j in res: # 2 -> 4 -> 8, O(2^n)
    #             l = j[:]
    #             l.append(i)
    #             tmp.append(l)
    #         res += tmp
    #
    #     return res

    # optimal iterative
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
    #     for num in nums:
    #         res += [ subset + [num] for subset in res]
    #     return res

    # recursive, backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
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
        expected = [[]]
        result = s.subsets(nums)
        self.assertListEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
