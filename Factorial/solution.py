import unittest
from typing import List, Optional


class Solution:

    # recursive, time: O(n), space: O(n)
    def factorial(self, n: int) -> int:
        return 1 if n <= 1 else n * self.factorial(n - 1)

    # iterative, time: O(n), space: O(1)
    def factorial(self, n: int) -> int:
        res = 1
        while n > 1:
            res = res * n
            n -= 1
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertEqual(s.factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
