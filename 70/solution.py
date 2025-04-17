import unittest
from typing import Dict, List, Optional


class Solution:
    # # time: O(n), space: O(n), time w/o memoization would be O(2^n)
    # def climbStairs(self, n: int) -> int:
    #     self.cache = {}
    #
    #     def search(n, stairs) -> int:
    #         if stairs in self.cache:
    #             return self.cache[stairs]
    #
    #         if n == stairs:
    #             return 1
    #         if n < stairs:
    #             return 0
    #
    #         paths = search(n, stairs + 1) + search(n, stairs + 2)
    #         self.cache[stairs] = paths
    #         return paths
    #
    #     return search(n, 1) + search(n, 2)

    # DP, iternative approach, time: O(n), space: O(1)
    # def climbStairs(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #
    #     prev1, prev2 = 2, 1
    #
    #     for _ in range(3, n + 1):
    #         prev1, prev2 = prev1 + prev2, prev1
    #     return prev1

    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # def climbStairs(self, n: int) -> int:
    #     def _climbStairs(n: int, cache: Dict):
    #         if n == 1:
    #             return 1
    #         if n == 2:
    #             return 2
    #
    #         if not n in cache:
    #             cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    #
    #         return cache[n]
    #
    #     return _climbStairs(n, {})

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        a, b = 2, 1

        for _ in range(n - 2):
            a, b = a + b, a

        return a


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.climbStairs(1), 1)
        self.assertEqual(s.climbStairs(2), 2)
        self.assertEqual(s.climbStairs(3), 3)
        self.assertEqual(s.climbStairs(4), 5)
        self.assertEqual(s.climbStairs(5), 8)
        self.assertEqual(s.climbStairs(6), 13)


if __name__ == "__main__":
    unittest.main()
