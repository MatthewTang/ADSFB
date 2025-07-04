import unittest
from typing import List, Optional


class Solution:
    # # time: O(nlogn)
    # def countBits(self, n: int) -> List[int]:
    #     # time: O(log(n))
    #     def _countBits(n: int) -> int:
    #         c = 0
    #         while n:
    #             c += 1 if n & 1 else 0
    #             n >>= 1
    #         return c
    #
    #     res = []
    #     # O(n)
    #     for i in range(n + 1):
    #         res.append(_countBits(i))  # O(log(i))
    #     return res

    # # time: O(n)
    # def countBits(self, n: int) -> List[int]:
    #     # time: O(1)
    #     def _countBits(n: int) -> int:
    #         c = 0
    #         for i in range(17):
    #             b = 1 << i
    #             if b & n:
    #                 c += 1
    #         return c
    #
    #     res = []
    #     # O(n)
    #     for i in range(n + 1):
    #         res.append(_countBits(i))  # O(1)
    #     return res

    # dp: time: O(n)
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2
            dp[i] = 1 + dp[i - offset]
        return dp


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 2
        expected = [0, 1, 1]
        result = s.countBits(n)
        self.assertListEqual(result, expected)

    def test2(self):
        s = Solution()
        n = 5
        expected = [0, 1, 1, 2, 1, 2]
        result = s.countBits(n)
        self.assertListEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
