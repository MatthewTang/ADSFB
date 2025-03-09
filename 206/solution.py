import unittest
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val: int = val
        self.next: Optional["ListNode"] = next

    def to_list(self) -> list:
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result

    def __repr__(self) -> str:
        return str(self.to_list())


class Solution:
    # Iterative
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     curr = head
    #     prev = None
    #     while curr:
    #         tmp = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = tmp
    #     return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def func(curr, prev):
            nextNode = curr.next
            curr.next = prev
            return curr if not nextNode else func(nextNode, curr)

        return func(head, None) if head else None


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        head = None
        self.assertEqual(str(s.reverseList(head)), str(None))

    def test2(self):
        s = Solution()
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        self.assertEqual(str(s.reverseList(head)), str([5, 4, 3, 2, 1]))

    def test3(self):
        s = Solution()
        head = ListNode(1, ListNode(2))
        self.assertEqual(str(s.reverseList(head)), str([2, 1]))

    def test4(self):
        s = Solution()
        head = ListNode()
        self.assertEqual(str(s.reverseList(head)), str([0]))


if __name__ == "__main__":
    unittest.main()
