import unittest
from typing import Dict, List, Optional
from Tree.solution import TreeNode


class Solution:
    # # brute force, time: O(n^2), ie n, n-1, n-2,...1. space: O(n)
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     if len(inorder) == 0:
    #         return
    #
    #     v = preorder[0]
    #     node = TreeNode(v)
    #     i = inorder.index(v) # O(n)
    #     node.left = self.buildTree(preorder[1 : 1 + i], inorder[:i])
    #     node.right = self.buildTree(preorder[1 + i :], inorder[i + 1 :])
    #
    #     return node

    # time: O(n^2), space: O(n), tricked grok/claude sonnet 37...
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     def _buildTree(
    #         preorder: List[int], inorder: List[int], index_map: Dict[int, int]
    #     ) -> Optional[TreeNode]:
    #         if len(inorder) == 0:
    #             return
    #
    #         v = preorder[0]
    #         node = TreeNode(v)
    #         i = index_map[v]  # O(1)
    #         node.left = self.buildTree(preorder[1 : 1 + i], inorder[:i])
    #         node.right = self.buildTree(preorder[1 + i :], inorder[i + 1 :])
    #
    #         return node
    #
    #     # make map
    #     index_map: Dict[int, int] = {}
    #     for i in range(len(inorder)):
    #         index_map[inorder[i]] = i
    #
    #     return _buildTree(preorder, inorder, index_map)

    # time: O(n), space O(n)
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     def _buildTree(
    #         index_map: Dict[int, int],
    #         p: int,
    #         start: int,
    #         end: int,
    #     ) -> Optional[TreeNode]:
    #         if start > end:
    #             return
    #
    #         v = preorder[p]
    #         node = TreeNode(v)
    #         i = index_map[v]  # O(1)
    #         if start == end:
    #             return node
    #
    #         # Left subtree: p + 1 is next position after root
    #         node.left = _buildTree(index_map, p + 1, start, i - 1)
    #
    #         # Right subtree: skip root (1) + left subtree size (i - start)
    #         node.right = _buildTree(index_map, p + 1 + (i - start), i + 1, end)
    #
    #         return node
    #
    #     # make map
    #     index_map: Dict[int, int] = {}
    #     for i in range(len(inorder)):
    #         index_map[inorder[i]] = i
    #
    #     return _buildTree(index_map, 0, 0, len(preorder) - 1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {v: i for i, v in enumerate(inorder)}
        c = 0

        def dfs(l, r):
            nonlocal c
            if l > r:
                return

            v = preorder[c]
            i = indices[v]
            node = TreeNode(v)
            c += 1
            node.left = dfs(l, i - 1)
            node.right = dfs(i + 1, r)

            return node

        return dfs(0, len(inorder) - 1)


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        result = s.buildTree(preorder, inorder)
        self.assertEqual(result, expected)

    def test2(self):
        s = Solution()
        preorder = [-1]
        inorder = [-1]
        expected = TreeNode(-1)
        result = s.buildTree(preorder, inorder)
        self.assertEqual(result, expected)

    def test3(self):
        s = Solution()
        preorder = [1, 2, 3]
        inorder = [2, 3, 1]
        expected = TreeNode(1, TreeNode(2, None, TreeNode(3)))
        result = s.buildTree(preorder, inorder)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
