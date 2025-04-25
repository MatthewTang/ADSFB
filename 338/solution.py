import unittest
from typing import List, Optional


class Solution:
    # time: O(nlogn)
    def countBits(self, n: int) -> List[int]:
        # time: O(log(n))
        def _countBits(n: int) -> int:
            c = 0
            while n:
                c += 1 if n & 1 else 0
                n >>= 1
            return c

        res = []
        # O(n)
        for i in range(n + 1):
            res.append(_countBits(i))  # O(log(i))
        return res


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
