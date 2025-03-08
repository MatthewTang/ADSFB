import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def getNode(self, index: int) -> ListNode:
        i = 0
        curr = self.head
        while i < index and curr:
            curr = curr.next
            i += 1
        return curr if curr else None

    def get(self, index: int) -> int:
        return self.getNode(index).val if self.getNode(index) else -1

    def insertHead(self, val: int) -> None:
        n = ListNode(val, self.head)
        self.head = n
        if not self.tail:
            self.tail = n

    def insertTail(self, val: int) -> None:
        n = ListNode(val)
        if self.tail:
            self.tail.next = n
        self.tail = n
        if not self.head:
            self.head = n

    def remove(self, index: int) -> bool:
        # if self.head is None or self.tail is None:
        #     return False
        if index == 0:
            if self.head.next is None:
                self.tail = None
            self.head = self.head.next
            return True

        target = self.getNode(index)
        if not target:
            return False

        prev = self.getNode(index - 1)
        if prev.next.next is None:
            self.tail = prev
        prev.next = prev.next.next if prev.next else None
        return True

    def getValues(self) -> List[int]:
        l = []
        curr = self.head
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
