import unittest
from typing import List, Optional


class ListNode:
    def __init__(
        self,
        val: int,
        next: Optional["ListNode"] = None,
        prev: Optional["ListNode"] = None,
    ) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = next
        self.prev: Optional["ListNode"] = prev


class Deque:
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self) -> bool:
        return self.head is None and self.tail is None

    def append(self, value: int) -> None:
        if not self.head:
            self.head = self.tail = ListNode(value)
        else:
            node = ListNode(value, None, self.tail)
            self.tail.next = node
            self.tail = node

    def appendleft(self, value: int) -> None:
        if not self.head:
            self.head = self.tail = ListNode(value)
        else:
            node = ListNode(value, self.head)
            self.head.prev = node
            self.head = node

    def pop(self) -> int:
        if self.tail:
            tail = self.tail
            prev = tail.prev
            if prev:
                prev.next = None
                self.tail = prev
            else:
                self.head = self.tail = None
            return tail.val
        return -1

    def popleft(self) -> int:
        if self.head:
            head = self.head
            next = head.next
            if next:
                next.prev = None
                self.head = next
            else:
                self.head = self.tail = None
            return head.val
        return -1

    def getValues(self) -> List[int]:
        l = []
        curr = self.head
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l


class Test(unittest.TestCase):
    def test1(self):
        d = Deque()
        self.assertTrue(d.isEmpty())
        self.assertIsNone(d.append(10))
        self.assertFalse(d.isEmpty())
        self.assertIsNone(d.appendleft(20))
        self.assertIs(d.popleft(), 20)
        self.assertIs(d.pop(), 10)
        self.assertIs(d.pop(), -1)
        self.assertIsNone(d.append(30))
        self.assertIs(d.pop(), 30)
        self.assertTrue(d.isEmpty())

    def test2(self):
        d = Deque()
        self.assertIsNone(d.appendleft(1))
        self.assertIsNone(d.appendleft(2))
        self.assertIs(d.pop(), 1)
        self.assertIs(d.pop(), 2)


if __name__ == "__main__":
    unittest.main()
