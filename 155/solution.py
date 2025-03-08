import unittest
from typing import List


# # brute force, time complexity for get min O(n)
# class MinStack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, val: int) -> None:
#         self.stack.append(val)
#
#     def pop(self) -> None:
#         return self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return min(self.stack)


# two stacks, time complexity for get min O(1), space complexity O(2n)
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(
            min(val, self.getMin() if self.getMin() is not None else float("infinity"))
        )

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]


class TestSolution(unittest.TestCase):
    def test1(self):
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertEqual(ms.getMin(), -3)
        ms.pop()
        self.assertEqual(ms.top(), 0)
        self.assertEqual(ms.getMin(), -2)

    def test2(self):
        ms = MinStack()
        ms.push(0)
        ms.push(1)
        ms.push(0)
        self.assertEqual(ms.getMin(), 0)
        ms.pop()
        self.assertEqual(ms.getMin(), 0)


if __name__ == "__main__":
    unittest.main()
