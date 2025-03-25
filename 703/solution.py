import unittest
from typing import List, Optional


# # naive
# class KthLargest:
#     # O(nlog(n)), space: O(n)
#     def __init__(self, k: int, nums: List[int]) -> None:
#         self.arr = sorted(nums)
#         self.k = k
#         pass
#
#     # O(nlog(n))
#     def add(self, val: int) -> int:
#         self.arr.append(val)
#         self.arr = sorted(self.arr)
#         return self.arr[-self.k]

# optimal, maintain min heap of size k
class KthLargest:
    # O(nlog(n))
    def __init__(self, k: int, nums: List[int]) -> None:
        self.arr = sorted(nums + [-float("infinity")])[-k:]
        pass

    # O(mlog(k)), m is no. of times add() called, k is the size of the array
    def add(self, val: int) -> int:
        if self.arr[0] >= val:
            return self.arr[0]
        else:
            self.arr[0] = val
            self.arr = sorted(self.arr)
            return self.arr[0]


class Test(unittest.TestCase):
    def test1(self):
        s = KthLargest(3, [4, 5, 8, 2])
        self.assertIs(s.add(3), 4)
        self.assertIs(s.add(5), 5)
        self.assertIs(s.add(10), 5)
        self.assertIs(s.add(9), 8)
        self.assertIs(s.add(4), 8)

    def test2(self):
        s = KthLargest(4, [7, 7, 7, 7, 8, 3])
        self.assertIs(s.add(2), 7)
        self.assertIs(s.add(10), 7)
        self.assertIs(s.add(9), 7)
        self.assertIs(s.add(9), 8)

    def test3(self):
        s = KthLargest(1, [])
        self.assertIs(s.add(-3), -3)
        self.assertIs(s.add(-2), -2)
        self.assertIs(s.add(-4), -2)
        self.assertIs(s.add(0), 0)
        self.assertIs(s.add(4), 4)


if __name__ == "__main__":
    unittest.main()
