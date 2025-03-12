import unittest
from typing import List, Optional, Deque
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue: Deque[List[int]] = deque([[pref, -1] for pref in students])
        topSandwich = 0
        while topSandwich < len(sandwiches) and queue:
            topStudent = queue.popleft()
            if topStudent[1] == topSandwich:
                return len(queue) + 1

            if topStudent[0] == sandwiches[topSandwich]:
                topSandwich += 1
            else:
                queue.append([topStudent[0], topSandwich])

        return 0

    # try ring buffer


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        students = [1, 1, 0, 0]
        sandwiches = [0, 1, 0, 1]
        print(s.countStudents(students, sandwiches))

    def test2(self):
        s = Solution()
        students = [1, 1, 1, 0, 0, 1]
        sandwiches = [1, 0, 0, 0, 1, 1]
        print(s.countStudents(students, sandwiches))

    def test3(self):
        s = Solution()
        students = [1, 1, 1, 0, 0, 1]
        sandwiches = [1, 0, 0, 1, 1, 1]
        print(s.countStudents(students, sandwiches))


if __name__ == "__main__":
    unittest.main()
