import unittest
from typing import Optional
from Tree.solution import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        if root.val == target:
            return True

        if root.val > target:
            return self.searchBST(root.left, target)
        else:
            return self.searchBST(root.right, target)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(2, TreeNode(1), TreeNode(3, None, TreeNode(4)))
        self.assertTrue(s.searchBST(root, 3))

    def test1(self):
        s = Solution()
        root = TreeNode(2, TreeNode(1), TreeNode(4, None, TreeNode(5)))
        self.assertFalse(s.searchBST(root, 3))


if __name__ == "__main__":
    unittest.main()
