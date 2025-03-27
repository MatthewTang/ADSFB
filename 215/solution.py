import unittest
from typing import List, Optional
import heapq


class Solution:
    # # time: O(n + (n-k)*logn + logk) = O(nlogn), space: O(1)
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     heap = nums
    #     heapq.heapify(heap)  # O(n)
    #     while len(heap) > k:  # (O(n-k)
    #         heapq.heappop(heap)  # O(logn)
    #     return heapq.heappop(heap)  # O(logk)

    # time: O(n*(1+logk) + (n-k)*logk + logk) = O(nlogk), space: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        while len(nums):  # O(n)
            n = nums.pop()  # O(1)
            heapq.heappush(heap, n)  # O(logk)
            if len(heap) > k:  # O(n-k)
                heapq.heappop(heap)  # O(logk)

        return heapq.heappop(heap)  # O(logk)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        expected = 5
        result = s.findKthLargest(nums, k)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        expected = 4
        result = s.findKthLargest(nums, k)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
