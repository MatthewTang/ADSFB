import unittest
from typing import List, Optional


class Solution:

    # native recursive, time: O(n), space: O(n)
    def factorial(self, n: int) -> int:
        return 1 if n <= 1 else n * self.factorial(n - 1)

    # iterative, time: O(n), space: O(1)
    def factorial(self, n: int) -> int:
        res = 1
        while n > 1:
            res = res * n
            n -= 1
        return res

    # Tail-recursive factorial: time O(n), space O(n) without TCO, O(1) with TCO (Python: O(n))
    def factorial(self, n: int, acc: int = 1) -> int:
        return acc if n <= 1 else self.factorial(n - 1, n * acc)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
