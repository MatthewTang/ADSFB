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

    # O(h), O(log(n)) always balanced tree
    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return None

        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]

        self.heap[1] = self.heap.pop()

        i = 1
        while True:
            l = i * 2
            r = i * 2 + 1

            if l >= len(self.heap):
                break

            if r < len(self.heap):
                m = min(self.heap[i], self.heap[l], self.heap[r])
                if self.heap[i] == m:
                    break
                if self.heap[l] == m:
                    self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                    i = l
                    continue
                if self.heap[r] == m:
                    self.heap[i], self.heap[r] = self.heap[r], self.heap[i]
                    i = r
                    continue

            m = min(self.heap[i], self.heap[l])
            if self.heap[i] == m:
                break
            if self.heap[l] == m:
                self.heap[i], self.heap[l] = self.heap[l], self.heap[i]
                i = l
                continue

        return res

    def __repr__(self) -> str:
        return str(self.heap[1:])


class Test(unittest.TestCase):
    def test1(self):
        h = Heap()
        h.push(19)
        h.push(16)
        h.push(14)
        h.push(21)
        h.push(26)
        h.push(19)
        h.push(68)
        h.push(65)
        h.push(13)
        self.assertIs(h.pop(), 13)
        self.assertIs(h.pop(), 14)
        self.assertIs(h.pop(), 16)
        self.assertIs(h.pop(), 19)
        h.push(50)
        self.assertIs(h.pop(), 19)
        self.assertIs(h.pop(), 21)
        self.assertIs(h.pop(), 26)
        self.assertIs(h.pop(), 50)
        self.assertIs(h.pop(), 65)
        h.push(10)
        self.assertIs(h.pop(), 10)
        self.assertIs(h.pop(), 68)
        h.push(19)
        self.assertIs(h.pop(), 19)
        self.assertIs(h.pop(), None)

    def test2(self):
        h = Heap()
        self.assertIs(h.pop(), None)


if __name__ == "__main__":
    unittest.main()
