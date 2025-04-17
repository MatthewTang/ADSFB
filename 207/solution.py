import unittest
from typing import List, Optional


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return


class Test(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertTrue(sol.canFinish(2, [[1, 0]]))

    def test2(self):
        sol = Solution()
        self.assertFalse(sol.canFinish(2, [[1, 0], [0, 1]]))


if __name__ == "__main__":
    unittest.main()
