import unittest
from typing import List, Optional
from Tree.solution import TreeNode


class Solution:
    def findMin(self, root: TreeNode) -> int:
        res = root.val
        while root.left:
            root = root.left
            res = root.val
        return res

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            right_min = self.findMin(root.right)
            root.val = right_min
            root.right = self.deleteNode(root.right, right_min)

        return root


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(
            5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7))
        )
        expected = TreeNode(5, TreeNode(4, TreeNode(2)), TreeNode(6, None, TreeNode(7)))
        result = s.deleteNode(root, 3)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        root = TreeNode(
            3,
            TreeNode(2),
            TreeNode(
                5, TreeNode(4), TreeNode(10, TreeNode(8, TreeNode(7)), TreeNode(15))
            ),
        )
        expected = TreeNode(
            3,
            TreeNode(2),
            TreeNode(7, TreeNode(4), TreeNode(10, TreeNode(8), TreeNode(15))),
        )
        result = s.deleteNode(root, 5)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
