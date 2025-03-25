import unittest
from typing import Optional, List
from collections import deque


class Heap:
    def __init__(self) -> None:
        self.heap = [0]

    # O(h), O(log(n)) always balanced tree
    def push(self, value: int) -> None:
        self.heap.append(value)
        i = len(self.heap) - 1

        # percolate up
        while self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def __repr__(self) -> str:
        return str(self.heap[1:])


class Test(unittest.TestCase):
    def test1(self):
        h = Heap()
        h.push(2)
        h.push(3)
        h.push(1)
        print(h)


if __name__ == "__main__":
    unittest.main()
