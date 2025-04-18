import unittest
from typing import List, Optional


class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     def _rob(i: int) -> int:
    #         if i >= len(nums):
    #             return 0
    #
    #         a = _rob(i + 2)
    #         b = _rob(i + 3)
    #
    #         return nums[i] + max(a, b)
    #
    #     return max(_rob(0), _rob(1))

    # w memoization (aka top-down dp)
    def rob(self, nums: List[int]) -> int:
        cache = [None] * len(nums)

        def _rob(i: int) -> int:
            if i >= len(nums):
                return 0

            if not cache[i]:
                a = _rob(i + 2)
                b = _rob(i + 3)

                cache[i] = nums[i] + max(a, b)

            return cache[i]

        res = max(_rob(0), _rob(1))
        # print(cache)
        return res

    # # bottom-up dp
    # def rob(self, nums: List[int]) -> int:
    #     l = len(nums)
    #     if l == 1:
    #         return nums[0]
    #     if l == 2:
    #         return max(nums[0], nums[1])
    #
    #     a, b, c = nums[-1], nums[-2], nums[-1] + nums[-3]
    #
    #     if l == 3:
    #         return max(b, c)
    #
    #     for i in range(4, l + 1):
    #         d = nums[-i] + max(a, b)
    #         a, b, c = b, c, d
    #
    #     return max(b, d)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [1, 2, 3, 1]
        expected = 4
        result = s.rob(nums)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [2, 7, 9, 3, 1]
        expected = 12
        result = s.rob(nums)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        nums = [10, 2, 7, 9, 7, 4]
        expected = 24
        result = s.rob(nums)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
