import unittest
from typing import List, Optional
from Tree.solution import TreeNode


# 19:45-19:57 (12mins)
class Solution:
    def searchBST(self, root: TreeNode, target:int) -> Optional[TreeNode]:
        if not root:
            return None
        if target > root.val:
            return self.searchBST(root.right, target)
        elif target < root.val:
            return self.searchBST(root.left, target)
        return root


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        self.assertEqual(s.searchBST(root, 2), TreeNode(2, TreeNode(1), TreeNode(3)))

    def test1(self):
        s = Solution()
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
        self.assertIsNone(s.searchBST(root, 8))


if __name__ == "__main__":
    unittest.main()
