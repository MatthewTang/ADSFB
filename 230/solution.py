import unittest
from typing import List, Optional
from Tree.solution import TreeNode


class Solution:
    # # aim O(n)
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # traverse inorder
    #     curr = root
    #     stack = []
    #     arr = []
    #
    #     # O(n)
    #     while curr or stack:
    #         while curr:
    #             stack.append(curr)
    #             curr = curr.left
    #         curr = stack.pop()
    #         arr.append(curr.val)
    #         curr = curr.right
    #
    #     return arr[k - 1]  # O(1)

    # iterative (optimal)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse inorder
        curr = root
        stack = []

        # O(n)
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        k = 1
        expected = 1
        result = s.kthSmallest(root, k)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        root = TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(5))
        k = 4
        expected = 5
        result = s.kthSmallest(root, k)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
