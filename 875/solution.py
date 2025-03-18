import unittest
from typing import List, Optional
import math


# 15:40
class Solution:
    # brute force, time: O(p*m), p = no. of piles, m = max val in piles. space: O(p)
    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     k = 1
    #     while sum([math.ceil(p / k) for p in piles]) > h:
    #         k += 1
    #     return k

    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     l, r = 1, max(piles)
    #
    #     while l < r:
    #         m = (l+r)//2
    #         t = sum([math.ceil(p / m) for p in piles])
    #         if t > h:
    #             l = m+1
    #         else:
    #             r = m
    #
    #     return l

    # time: O(p*log(m)), p = no. of piles, m = max val in piles. space: O(p)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # O(p)

        res = r
        while l <= r:
            m = (l+r)//2
            t = sum([math.ceil(p / m) for p in piles]) # O(p)
            if t > h:
                l = m+1
            else:
                res = m
                r = m-1

        return res


class Test(unittest.TestCase):
    # 1, 2, 3, 4
    # 3+6+7+11=27, 2+3+4+6=15, 1+2+3+4=10, 1+2+2+3=6
    def test1(self):
        s = Solution()
        piles = [3, 6, 7, 11]
        h = 8
        expected = 4
        result = s.minEatingSpeed(piles, h)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        piles = [30,11,23,4,20]
        h = 5
        expected = 30
        result = s.minEatingSpeed(piles, h)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        piles = [30,11,23,4,20]
        h = 6
        expected = 23 
        result = s.minEatingSpeed(piles, h)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
