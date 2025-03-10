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


class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr and curr != self.tail:
            if index == i:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        n = ListNode(val, self.head.next, self.head)
        self.head.next.prev = n
        self.head.next = n

    def addAtTail(self, val: int) -> None:
        n = ListNode(val, self.tail, self.tail.prev)
        self.tail.prev.next = n
        self.tail.prev = n

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        target = self.head.next
        while target and i < index:
            target = target.next
            i += 1
        if not target:
            return False
        prev = target.prev
        n = ListNode(val, prev.next, prev)
        prev.next.prev = n
        prev.next = n
        return True

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        target = self.head.next
        while target and i < index:
            target = target.next
            i += 1
        if not target or target == self.tail:
            return False
        prev = target.prev
        next = target.next
        prev.next = next
        next.prev = prev
        return True

    def getValues(self) -> List[int]:
        l = []
        curr = self.head.next
        while curr and curr != self.tail:
            l.append(curr.val)
            curr = curr.next
        return l


class Test(unittest.TestCase):
    def test1(self):
        ll = LinkedList()
        ll.addAtHead(1)
        ll.addAtTail(3)
        ll.addAtIndex(1, 2)
        print(ll.getValues())
        self.assertEqual(ll.get(1), 2)
        ll.deleteAtIndex(1)
        self.assertEqual(ll.get(1), 3)

    def test2(self):
        ll = LinkedList()
        ll.deleteAtIndex(0)

    def test3(self):
        ll = LinkedList()
        ll.addAtHead(1)
        self.assertEqual(ll.deleteAtIndex(0), True)

    def test4(self):
        ll = LinkedList()
        ll.addAtHead(7)
        ll.addAtHead(2)
        ll.addAtHead(1)
        ll.addAtIndex(3, 0)
        ll.deleteAtIndex(2)
        ll.addAtHead(6)
        ll.addAtTail(4)
        self.assertEqual(ll.get(4), 4)
        ll.addAtHead(4)
        ll.addAtIndex(5, 0)
        ll.addAtHead(6)

    def test4(self):
        ll = LinkedList()
        ll.addAtIndex(2, 1)
        ll.addAtIndex(3, 4)
        ll.addAtTail(1)
        ll.get(0)
        ll.deleteAtIndex(0)
        ll.get(0)


if __name__ == "__main__":
    unittest.main()
