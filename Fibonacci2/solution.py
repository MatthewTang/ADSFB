import unittest
from typing import List, Optional


class Solution:
    # def fib(self, n: int):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return self.fib(n-1) + self.fib(n-2)

    # def fib(self, n: int):
    #     a, b = 0, 1
    #     for _ in range(n + 1):
    #         a, b = a + b, a
    #     return b

    def fib(self, n: int):
        def _fib(n, a: int, b: int):
            if n == 0:
                return b

            return _fib(n - 1, a + b, a)

        return _fib(n + 1, 0, 1)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.fib(0), 0)
        self.assertEqual(s.fib(1), 1)
        self.assertEqual(s.fib(6), 8)
        self.assertEqual(s.fib(5), 5)
        self.assertEqual(s.fib(4), 3)


if __name__ == "__main__":
    unittest.main()
