import unittest
from typing import Dict, List, Optional
import sys
import traceback
from functools import lru_cache


class Solution:
    # def fib(self, n: int):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return self.fib(n - 1) + self.fib(n - 2)

    # # bottom-up dp
    # def fib(self, n: int):
    #     if n <= 1:
    #         return n
    #     a, b = 0, 1
    #     for _ in range(2, n + 1):
    #         a, b = b, a + b
    #     return b

    # # bottom-up dp optimised
    # def fib(self, n: int):
    #     a, b = 0, 1
    #     for _ in range(n + 1):
    #         a, b = a + b, a
    #     return b

    # def fib(self, n: int):
    #     def _fib(n, a: int, b: int):
    #         if n == 0:
    #             return b
    #
    #         return _fib(n - 1, a + b, a)
    #
    #     return _fib(n + 1, 0, 1)

    # top-down dp
    def fib(self, n: int):
        def memoizedFib(n: int, cache: Dict):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = self.fib(n - 1) + self.fib(n - 2)
            return cache[n]

        return memoizedFib(n, {})

    # @lru_cache
    # def fib(self, n: int):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return self.fib(n - 1) + self.fib(n - 2)


class Test(unittest.TestCase):
    # def test1(self):
    #     s = Solution()
    #     self.assertEqual(s.fib(0), 0)
    #     self.assertEqual(s.fib(1), 1)
    #     self.assertEqual(s.fib(6), 8)
    #     self.assertEqual(s.fib(5), 5)
    #     self.assertEqual(s.fib(4), 3)

    # test recursion limit w lru_cache vs cache dict
    def test2(self):
        s = Solution()
        try:
            # sys.setrecursionlimit(20000)
            s.fib(1000)
        except Exception as e:
            stack = traceback.extract_tb(sys.exc_info()[2])
            print(e)
            print(sys.getrecursionlimit())
            print(f"depth: {len(stack)}")
            print(e)


if __name__ == "__main__":
    unittest.main()
