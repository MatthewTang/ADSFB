import unittest
from typing import List, Optional
from Tree.solution import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        return root


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        expected = TreeNode(
            4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(5))
        )
        result = s.insertIntoBST(root, 5)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
