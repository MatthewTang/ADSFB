import unittest
from typing import List, Optional


class Solution:
    # # brute force n branches, has duplicates
    # def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     res = []
    #
    #     def dfs(cur: List[int], total: int):
    #         if total == target:
    #             if not sorted(cur) in res:
    #                 res.append(sorted(cur))
    #             return
    #         if total > target:
    #             return
    #         for i in nums:
    #             dfs(cur[:] + [i], total + i)
    #
    #     dfs([],0)
    #     return res

    # backtracking, 2 branches, no duplicates
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [3, 4, 5]
        target = 16
        expected = [[3, 3, 3, 3, 4], [3, 3, 5, 5], [4, 4, 4, 4], [3, 4, 4, 5]]
        result = s.combinationSum(nums, target)
        self.assertListEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
