import unittest
from typing import List, Optional


# 14:41 -> 14:54 (error) -> 15:03 (22min)
class Solution:
    def __init__(self, bad) -> None:
        self.bad = bad
        pass

    def isBadVersion(self, version: int) -> bool:
        if version >= self.bad:
            return True

        return False

    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        res = -1
        while l <= r:
            m = (l + r) // 2
            print(f"l: {l}, r: {r}, m: {m}")

            if self.isBadVersion(m):
                res = m
                r = m - 1
            else:
                l = m + 1

        return res


class Test(unittest.TestCase):
    def test1(self):
        bad = 4
        s = Solution(bad)
        n = 5
        result = s.firstBadVersion(n)
        self.assertIs(result, bad)

    def test2(self):
        bad = 1
        s = Solution(bad)
        n = 1
        result = s.firstBadVersion(n)
        self.assertIs(result, bad)

    # [g, b, b]
    def test3(self):
        bad = 2
        s = Solution(bad)
        n = 3
        result = s.firstBadVersion(n)
        self.assertIs(result, bad)

    def test4(self):
        bad = 1
        s = Solution(bad)
        n = 5
        result = s.firstBadVersion(n)
        self.assertIs(result, bad)


if __name__ == "__main__":
    unittest.main()
