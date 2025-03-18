from typing import Optional


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

    def __repr__(self) -> str:
        return str(self.val)

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


def main():
    node = TreeNode(1)
    print(node)


if __name__ == "__main__":
    main()
