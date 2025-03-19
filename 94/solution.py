import unittest
from typing import List, Optional
from Tree.solution import TreeNode


# time O(n), space O(h)
class Solution:

    # # recursion
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     res = []
    #
    #     def _traverse(root, l):
    #         if not root:
    #             return l
    #
    #         l = _traverse(root.left, l)
    #         l.append(root.val)
    #         l = _traverse(root.right, l)
    #
    #         return l
    #
    #     return _traverse(root, res)

    # iteration
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        expected = [1, 3, 2]
        result = s.inorderTraversal(root)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))),
            TreeNode(3, None, TreeNode(8, TreeNode(9))),
        )
        expected = [4, 2, 6, 5, 7, 1, 3, 9, 8]
        result = s.inorderTraversal(root)
        self.assertEqual(result, expected)

    def test3(self):
        s = Solution()
        root = None
        expected = []
        result = s.inorderTraversal(root)
        self.assertEqual(result, expected)

    def test4(self):
        s = Solution()
        root = TreeNode(1)
        expected = [1]
        result = s.inorderTraversal(root)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
