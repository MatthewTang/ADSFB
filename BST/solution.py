import unittest
from typing import Optional
from Tree.solution import TreeNode


class Solution:
    # time: O(logN), assume the tree is balanced ie height of left and right subtree is almost equal/differs by 1
    # time: worst case: O(N), skewed tree, ie height of left or right subtree is N
    # time: O(h), h is the height of the tree, h = logN if the tree is balanced
    # space: O(logN), recursive stack, if tail recursion is optimized, then O(1)
    def searchBST(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False

        if root.val > target:
            return self.searchBST(root.left, target)
        elif root.val < target:
            return self.searchBST(root.right, target)
        else:
            return True


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(2, TreeNode(1), TreeNode(3, None, TreeNode(4)))
        self.assertTrue(s.searchBST(root, 3))

    def test2(self):
        s = Solution()
        root = TreeNode(2, TreeNode(1), TreeNode(4, None, TreeNode(5)))
        self.assertFalse(s.searchBST(root, 3))


if __name__ == "__main__":
    unittest.main()
