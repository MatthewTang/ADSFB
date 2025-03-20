import unittest
from typing import List, Optional
from Tree.solution import TreeNode
from collections import deque


class Solution:
    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            res.append(l)
        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        expected = [[3],[9,20],[15,7]]
        result = s.bfs(root)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        root = TreeNode(1)
        expected = [[1]]
        result = s.bfs(root)
        self.assertEqual(result, expected)

    def test3(self):
        s = Solution()
        root = None
        expected = []
        result = s.bfs(root)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
