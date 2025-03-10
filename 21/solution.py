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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while list1 or list2:
            if not list1:
                curr.next = list2
                break
            if not list2:
                curr.next = list1
                break
            if list1.val <= list2.val:
                n = ListNode(list1.val)
                curr.next = n
                curr = n
                list1 = list1.next
            else:
                n = ListNode(list2.val)
                curr.next = n
                curr = n
                list2 = list2.next

        return head.next


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        head1 = ListNode(1, ListNode(2, ListNode(4)))
        head2 = ListNode(1, ListNode(3, ListNode(5)))
        self.assertEqual(str(s.mergeTwoLists(head1, head2)), str([1, 1, 2, 3, 4, 5]))


if __name__ == "__main__":
    unittest.main()
