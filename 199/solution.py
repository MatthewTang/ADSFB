import unittest
from typing import List, Optional
from Tree.solution import TreeNode
from collections import deque


class Solution:
    # time: O(n), space: O(n)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root] if root else [])
        res = []
        while q:
            l = []
            for _ in range(len(q)):
                curr = q.popleft()
                l.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(l[-1])
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(
            1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4))
        )
        expected = [1, 3, 4]
        result = s.rightSideView(root)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
        expected = [1,3,4,5]
        result = s.rightSideView(root)
        self.assertEqual(result, expected)

    def test3(self):
        s = Solution()
        root = TreeNode(1, None, TreeNode(3))
        expected = [1,3]
        result = s.rightSideView(root)
        self.assertEqual(result, expected)

    def test4(self):
        s = Solution()
        root = None
        expected = []
        result = s.rightSideView(root)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
