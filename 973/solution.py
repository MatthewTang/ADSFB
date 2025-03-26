import unittest
from typing import List, Optional
import heapq


# # naive solution
# class Solution:
#     # time: O(n) + O(n*log(n)) + O(n) + O(k) = O(n*log(n)), space: O(n)
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         return [
#             p[1]
#             for p in sorted(
#                 [[point[0] ** 2 + point[1] ** 2, point] for point in points],  # O(n)
#                 key=lambda x: x[0],  # O(n*log(n))
#             )  # O(n)
#         ][
#             :k
#         ]  # O(k)


# # min-heap
# class Solution:
#     # O(n) + O(n) + O(n*log(n)) = O(n*log(n)), space: O(n)
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         points = [[point[0] ** 2 + point[1] ** 2, point] for point in points]  # O(n)
#         heapq.heapify(points)  # O(n)
#         res = []
#         while k > 0:  # O(k) = O(n)
#             res.append(heapq.heappop(points)[1])  # O(log(n))
#             k -= 1
#         return res

# max-heap of size k
class Solution:
    # time: O(n*logk + (n-k)*logk + k) = O(n*logk), space: O(k)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        while len(points):  # O(n)
            point = points.pop()
            heapq.heappush(heap, [-(point[0] ** 2 + point[1] ** 2), point])  # O(logk)
            if len(heap) > k:  # O(n-k)
                heapq.heappop(heap)  # O(logk)

        return [p[1] for p in heap]  # O(k)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        points = [[1, 3], [-2, 2]]
        k = 1
        expected = [[-2, 2]]
        result = s.kClosest(points, k)
        self.assertListEqual(sorted(result), sorted(expected))

    def test2(self):
        s = Solution()
        points = [[3, 3], [5, -1], [-2, 4]]
        k = 2
        expected = [[3, 3], [-2, 4]]
        result = s.kClosest(points, k)
        self.assertListEqual(sorted(result), sorted(expected))


if __name__ == "__main__":
    unittest.main()
