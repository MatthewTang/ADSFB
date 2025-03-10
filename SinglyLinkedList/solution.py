import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = next


class LinkedList:
    def __init__(self):
        self.head = self.tail = ListNode(-1)

    def getNode(self, index: int) -> ListNode:
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1
        return curr if curr else None

    def get(self, _index: int) -> int:
        index = _index + 1
        return self.getNode(index).val if self.getNode(index) else -1

    def insertHead(self, val: int) -> None:
        n = ListNode(val, self.head.next)
        if not self.head.next:
            self.tail = n
        self.head.next = n

    def insertTail(self, val: int) -> None:
        n = ListNode(val)
        self.tail.next = n
        self.tail = n

    def remove(self, index: int) -> bool:
        prev = self.getNode(index)
        if not prev:
            return False
        target = prev.next
        if not target:
            return False
        if not target.next:
            self.tail = prev
        prev.next = target.next
        return True

    def getValues(self) -> List[int]:
        l = []
        curr = self.head.next
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l


class Test(unittest.TestCase):
    def test1(self):
        ll = LinkedList()
        ll.insertHead(1)
        ll.insertTail(2)
        ll.insertHead(0)
        ll.remove(1)
        self.assertEqual(ll.getValues(), [0, 2])

    def test2(self):
        ll = LinkedList()
        ll.insertHead(1)
        ll.insertTail(2)
        self.assertEqual(ll.get(5), -1)

    def test3(self):
        ll = LinkedList()
        ll.insertHead(1)
        self.assertEqual(ll.remove(0), True)

    def test4(self):
        ll = LinkedList()
        ll.insertTail(1)
        ll.insertTail(2)
        self.assertEqual(ll.get(1), 2)
        self.assertEqual(ll.remove(1), True)
        ll.insertTail(2)
        self.assertEqual(ll.get(1), 2)
        self.assertEqual(ll.get(0), 1)

    def test4(self):
        ll = LinkedList()
        self.assertEqual(ll.remove(1), False)

    def test5(self):
        ll = LinkedList()
        ll.insertHead(1)
        self.assertEqual(ll.remove(2), False)
        self.assertEqual(ll.remove(1), False)


if __name__ == "__main__":
    unittest.main()
