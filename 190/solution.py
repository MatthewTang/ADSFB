import unittest
from typing import List, Optional


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1
            res |= 1 if n & 1 else 0
            n >>= 1
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 43261596
        expected = 964176192
        result = s.reverseBits(n)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        n = 4294967293
        expected = 3221225471
        result = s.reverseBits(n)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
