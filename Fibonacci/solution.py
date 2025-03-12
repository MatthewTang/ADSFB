import unittest
from typing import List, Optional


class Solution:

    # # Naive recursive Fibonacci: time O(φ^n) [approx O(2^n)], space O(n) - max stack depth
    # def fib(self, n: int) -> int:
    #     if n <= 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return self.fib(n - 1) + self.fib(n - 2)

    # # iterative, time: O(n), space: O(1)
    # def fib(self, n: int) -> int:
    #     if n <= 1:
    #         return n
    #     a, b = 0, 1
    #     for _ in range(2, n + 1):
    #         a, b = b, a + b
    #     return b

    # tail-recursive, time O(n), space O(1) w/ TCO, O(n) in Python
    def fib(self, n: int, a: int = 0, b: int = 1) -> int:
        if n <= 0:
            return a
        if n == 1:
            return b
        return self.fib(n - 1, b, a + b)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.fib(6), 8)
        self.assertEqual(s.fib(5), 5)
        self.assertEqual(s.fib(4), 3)


if __name__ == "__main__":
    unittest.main()
