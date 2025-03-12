import unittest
from typing import List, Optional, Deque
from collections import deque


class MyStack:
    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()
        pass

    # O(n) where n is the number of elements myStack has
    def push(self, x: int) -> None:
        if len(self.q1) == 0:  # O(1)
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
        else:
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())

    def pop(self) -> int: # O(1)
        if self.empty():
            return
        if len(self.q1) == 0:
            return self.q2.popleft()
        else:
            return self.q1.popleft()

    def top(self) -> int: # O(1)
        if self.empty():
            return
        if len(self.q1) == 0:
            return self.q2[0]
        else:
            return self.q1[0]

    def empty(self) -> bool: # O(1)
        return len(self.q1) == 0 and len(self.q2) == 0


class Test(unittest.TestCase):
    def test1(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertFalse(s.empty())


if __name__ == "__main__":
    unittest.main()
