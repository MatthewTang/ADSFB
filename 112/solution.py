import unittest
from typing import List, Optional
from Tree.solution import TreeNode


class Solution:
    # # brute force, O(n) + O(k*h) + O(k*h) + O(k) = O(n) + O(k*h) = O(nlogn)
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     leafPaths = []
    #     self.leafPaths(root, [], leafPaths)  # O(n) + O(k*h)
    #     sums = [sum(l) for l in leafPaths]  # O(k*h)
    #     return targetSum in sums  # O(k)

    # brute force, O(n) + O(k*h)
    # best: O(n) + O(n) = O(n)
    # worst: O(n) + O(nlogn) = O(nlogn)
    def leafPaths(
        self, root: Optional[TreeNode], l: List[int], res: List[List[int]]
    ) -> List[List[int]]:
        if not root:
            return

        l.append(root.val)
        if not root.left and not root.right:  # O(k), k no. of leaves, 1 - n/2
            res.append(l[:])  # O(h), h height, n - log(n)
        self.leafPaths(root.left, l, res)
        self.leafPaths(root.right, l, res)
        l.pop()

    # time: O(n), space: O(h) = O(n)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        remaining = targetSum - root.val
        if not root.right and not root.left:
            if remaining == 0:
                return True
            else:
                return False
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(
            root.right, remaining
        )


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
        )
        paths = []
        s.leafPaths(root, [], paths)
        self.assertListEqual(
            sorted(paths),
            sorted([[5, 4, 11, 7], [5, 4, 11, 2], [5, 8, 13], [5, 8, 4, 1]]),
        )

    def test2(self):
        s = Solution()
        root = None
        paths = []
        s.leafPaths(root, [], paths)
        self.assertEqual(paths, [])

    def test3(self):
        s = Solution()
        root = TreeNode(
            5,
            TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
            TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))),
        )
        self.assertTrue(s.hasPathSum(root, 22))

    def test4(self):
        s = Solution()
        root = TreeNode(
            1,
            TreeNode(2),
            TreeNode(3),
        )
        self.assertEqual(s.hasPathSum(root, 5), False)

    def test5(self):
        s = Solution()
        root = None
        self.assertEqual(s.hasPathSum(root, 0), False)

    def test6(self):
        s = Solution()
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(s.hasPathSum(root, 1), False)


if __name__ == "__main__":
    unittest.main()
