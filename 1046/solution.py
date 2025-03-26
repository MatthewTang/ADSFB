import unittest
from typing import List, Optional
import heapq


# # naive
# class Solution:
#     # time: O(n*logn) + O(n*n*logn) = O(n^2*log(n)), space: O(n)
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         s = sorted(stones)  # O(n*logn)
#         # O(n-1)
#         while len(s) > 1:
#             a, b = s[-2:]  # O(2)
#             if a == b:
#                 s = s[:-2]
#             else:
#                 s = s[:-2]  # O(n-2)
#                 s.append(abs(a - b))  # O(1)
#                 s = sorted(s)  # O(n-1*log(n-1))
#
#         return s[0] if len(s) == 1 else 0


# use max heap
class Solution:
    # time: O(n) + O(n) + O(n*log(n)) = O(n*log(n)), space: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]  # O(n)
        heapq.heapify(stones)  # O(n)
        while len(stones) > 1:  # O(n)
            a = -heapq.heappop(stones)  # O(log(n))
            b = -heapq.heappop(stones)  # O(log(n))
            if a == b:
                continue
            else:
                heapq.heappush(stones, -abs(a - b))  # O(log(n))

        return -stones[0] if len(stones) == 1 else 0  # O(1)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        stones = [2, 7, 4, 1, 8, 1]
        expected = 1
        result = s.lastStoneWeight(stones)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        stones = [1]
        expected = 1
        result = s.lastStoneWeight(stones)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        stones = [2, 2]
        expected = 0
        result = s.lastStoneWeight(stones)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
