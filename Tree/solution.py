import unittest
from typing import Optional, List


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    # print tree graph
    def __repr__(self) -> str:
        result = f"TreeNode({self.val}"
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

            lines = [f"{prefix}{'└── ' if is_tail else '├── '}{node.val}"]

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


# time: O(logn), space: O(logn), recursive call stack with TCO
def insert(root: Optional[TreeNode], val: int) -> TreeNode:
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)

    return root


# time: O(logn), space: O(1)
def findMin(root: TreeNode) -> int:
    res = root.val
    while root.left:
        root = root.left
        res = root.val
    return res


# time: O(logn), space: O(logn)
def remove(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        # root has 1 or 0 children
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # root has 2 children
        right_min = findMin(root.right)
        root.val = right_min
        root.right = remove(root.right, right_min)

    return root


# all of the following are DPS
# time: O(n)
def inorder(root: Optional[TreeNode], l: List[int] = []) -> List[int]:
    if not root:
        return l
    l = inorder(root.left, l)
    l.append(root.val)
    l = inorder(root.right, l)
    return l


def preorder(root: Optional[TreeNode], l: List[int] = []) -> List[int]:
    if not root:
        return l
    l.append(root.val)
    l = preorder(root.left, l)
    l = preorder(root.right, l)
    return l


def postorder(root: Optional[TreeNode], l: List[int] = []) -> List[int]:
    if not root:
        return l
    l = postorder(root.left, l)
    l = postorder(root.right, l)
    l.append(root.val)
    return l


# time: O(n)
def reverse_inorder(root: Optional[TreeNode], l: List[int] = []) -> List[int]:
    if not root:
        return l
    l = reverse_inorder(root.right, l)
    l.append(root.val)
    l = reverse_inorder(root.left, l)
    return l


def reverse_preorder(root: Optional[TreeNode], l: List[int] = []) -> List[int]:
    if not root:
        return l
    l.append(root.val)
    l = reverse_preorder(root.right, l)
    l = reverse_preorder(root.left, l)
    return l


def reverse_postorder(root: Optional[TreeNode], l: List[int] = []) -> List[int]:
    if not root:
        return l
    l = reverse_postorder(root.right, l)
    l = reverse_postorder(root.left, l)
    l.append(root.val)
    return l


def duplicate(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    node = TreeNode(root.val)
    node.left = duplicate(root.left)
    node.right = duplicate(root.right)
    return node


def duplicate_mirror(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return
    node = TreeNode(root.val)
    node.left = duplicate_mirror(root.right)
    node.right = duplicate_mirror(root.left)
    return node


def delete(root: Optional[TreeNode]):
    if not root:
        return
    root.left = delete(root.left)
    root.right = delete(root.right)
    root.val = 0
    return None


class Test(unittest.TestCase):
    def test1(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3, None, TreeNode(4)))
        output = insert(root, 5)
        expected = TreeNode(
            2, TreeNode(1), TreeNode(3, None, TreeNode(4, None, TreeNode(5)))
        )
        self.assertEqual(output, expected)

    def test2(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3, None, TreeNode(4)))
        output = findMin(root)
        expected = 1
        self.assertEqual(output, expected)

    def test3(self):
        root = TreeNode(2, TreeNode(1, TreeNode(0)), TreeNode(3, None, TreeNode(4)))
        output = findMin(root)
        expected = 0
        self.assertEqual(output, expected)

    def test4(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = remove(root, 2)
        expected = TreeNode(4, TreeNode(3), TreeNode(6, TreeNode(5), TreeNode(7)))
        self.assertEqual(output, expected)

    def test5(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = remove(root, 3)
        expected = TreeNode(4, TreeNode(2), TreeNode(6, TreeNode(5), TreeNode(7)))
        self.assertEqual(output, expected)

    def test6(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = remove(root, 4)
        expected = TreeNode(5, TreeNode(3, TreeNode(2)), TreeNode(6, None, TreeNode(7)))
        self.assertEqual(output, expected)

    def test7(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = remove(root, 6)
        expected = TreeNode(4, TreeNode(3, TreeNode(2)), TreeNode(7, TreeNode(5)))
        self.assertEqual(output, expected)

    def test8(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = inorder(root, [])
        expected = [2, 3, 4, 5, 6, 7]
        self.assertEqual(output, expected)

    def test9(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = preorder(root, [])
        expected = [4, 3, 2, 6, 5, 7]
        self.assertEqual(output, expected)

    def test10(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = postorder(root, [])
        expected = [2, 3, 5, 7, 6, 4]
        self.assertEqual(output, expected)

    def test11(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = reverse_inorder(root, [])
        expected = [7, 6, 5, 4, 3, 2]
        self.assertEqual(output, expected)

    def test12(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        output = duplicate(root)
        # output = root
        # print(id(output))
        # print(id(root))
        self.assertEqual(output, root)
        self.assertIsNot(output, root)

    def test13(self):
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, TreeNode(5), TreeNode(7))
        )
        mirror = duplicate_mirror(root)
        self.assertEqual(inorder(mirror, []), reverse_inorder(root, []))
        self.assertEqual(preorder(root, []), reverse_preorder(mirror, []))

    def test14(self):
        node5= TreeNode(5)
        root = TreeNode(
            4, TreeNode(3, TreeNode(2)), TreeNode(6, node5, TreeNode(7))
        )
        output = delete(root)
        self.assertIsNone(output)
        self.assertIsNone(root.right)
        self.assertIsNone(root.left)
        self.assertEqual(root.val, 0)
        self.assertIsNone(node5.right)
        self.assertIsNone(node5.left)
        self.assertEqual(node5.val, 0)


if __name__ == "__main__":
    unittest.main()
