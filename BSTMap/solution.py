import unittest
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        key: int,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        result = f"TreeNode({self.key},{self.val}"
        if self.left or self.right:
            result += f", {self.left.__repr__() if self.left else 'None'}"
            result += f", {self.right.__repr__() if self.right else 'None'}"
        result += ")"
        return result

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return (
            self.val == other.val
            and (
                (self.left is None and other.left is None) or (self.left == other.left)
            )
            and (
                (self.right is None and other.right is None)
                or (self.right == other.right)
            )
        )

    def draw_tree(self) -> str:
        def _build_lines(node, prefix="", is_tail=True):
            if not node:
                return []

            lines = [f"{prefix}{'└── ' if is_tail else '├── '}({node.key},{node.val})"]

            children = []
            if node.left:
                children.append((node.left, "left"))
            if node.right:
                children.append((node.right, "right"))

            for i, (child, _) in enumerate(children[:-1] if children else []):
                new_prefix = prefix + ("    " if is_tail else "│   ")
                lines.extend(_build_lines(child, new_prefix, False))

            if children:
                last_child, _ = children[-1]
                new_prefix = prefix + ("    " if is_tail else "│   ")
                lines.extend(_build_lines(last_child, new_prefix, True))

            return lines

        lines = _build_lines(self)
        return "\n".join(lines)


def insert(root: Optional[TreeNode], key: int, val: int) -> TreeNode:
    if not root:
        return TreeNode(key, val)
    if key > root.key:
        root.right = insert(root.right, key, val)
    elif key < root.key:
        root.left = insert(root.left, key, val)
    else:
        root = TreeNode(key, val)

    return root


def findMin(root: TreeNode) -> TreeNode:
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


def remove(root: TreeNode, key: int) -> Optional[TreeNode]:
    if not root:
        return
    if key > root.key:
        root.right = remove(root.right, key)
    elif key < root.key:
        root.left = remove(root.left, key)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        rightMin = findMin(root.right)
        root.key = rightMin.key
        root.val = rightMin.val
        root.right = remove(root.right, rightMin.key)

    return root


class TreeMap:
    def __init__(self) -> None:
        self.root = None

    def insert(self, key: int, val: int) -> None:
        self.root = insert(self.root, key, val)

    # def insert(self, key: int, val: int) -> None:
    #     node = TreeNode(key, val)
    #     if not self.root:
    #         self.root = node
    #     else:
    #         curr = self.root
    #         while curr:
    #             if key > curr.key:
    #                 if not curr.right:
    #                     curr.right = node
    #                     return
    #                 else:
    #                     curr = curr.right
    #             elif key < curr.key:
    #                 if not curr.left:
    #                     curr.left = node
    #                     return
    #                 else:
    #                     curr = curr.left
    #             else:
    #                 return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.val
            if key > curr.key:
                curr = curr.right
            elif key < curr.key:
                curr = curr.left
        return -1

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = remove(self.root, key)

    def getInorderKeys(self) -> List[int]:
        l = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            dfs(root.left)
            l.append(root.key)
            dfs(root.right)

        dfs(self.root)

        return l


class Test(unittest.TestCase):
    def test1(self):
        tm = TreeMap()
        tm.insert(1, 2)
        self.assertEqual(tm.get(1), 2)
        tm.insert(4, 0)
        self.assertEqual(tm.getMin(), 2)
        self.assertEqual(tm.getMax(), 0)

    def test2(self):
        tm = TreeMap()
        tm.insert(1, 2)
        tm.insert(4, 2)
        tm.insert(3, 7)
        tm.insert(2, 1)
        self.assertEqual(tm.getInorderKeys(), [1, 2, 3, 4])
        tm.remove(1)
        self.assertEqual(tm.getInorderKeys(), [2, 3, 4])

    def test3(self):
        tm = TreeMap()
        self.assertEqual(tm.getMin(), -1)

    def test4(self):
        tm = TreeMap()
        tm.insert(1, 10)
        tm.insert(1, 20)
        self.assertEqual(tm.get(1), 20)


if __name__ == "__main__":
    unittest.main()
