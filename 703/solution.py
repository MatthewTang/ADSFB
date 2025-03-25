import unittest
from typing import List, Optional


# naive
class KthLargest:
    # O(nlog(n))
    def __init__(self, k: int, nums: List[int]) -> None:
        self.arr = sorted(nums)
        self.k = k
        pass

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr = sorted(self.arr)
        return self.arr[-self.k]


class Test(unittest.TestCase):
    def test1(self):
        s = KthLargest(3, [4, 5, 8, 2])
        self.assertIs(s.add(3), 4)
        self.assertIs(s.add(5), 5)
        self.assertIs(s.add(10), 5)
        self.assertIs(s.add(9), 8)
        self.assertIs(s.add(4), 8)


if __name__ == "__main__":
    unittest.main()
