import unittest
from typing import List, Optional


class Solution:
    def countBits(self, n):
        count = 0
        while n > 0:
            if n & 1 == 1:  # same as n %2 == 1
                count += 1
            n = n >> 1  # same as n //2
        return count


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        arg = 23
        expected = 4
        result = s.countBits(arg)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        arg = 24
        expected = 2
        result = s.countBits(arg)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
