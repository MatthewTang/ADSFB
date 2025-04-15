import unittest
from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Node):
            return False
        if self.val != __o.val:
            return False
        if len(self.neighbors) != len(__o.neighbors):
            return False
        for i in range(len(self.neighbors)):
            if self.neighbors[i].val != __o.neighbors[i].val:
                return False
        return True

    def __repr__(self) -> str:
        return f"Node({self.val}, [{', '.join(str(neighbor.val) for neighbor in self.neighbors)}])"


class Solution:
    # time complexity: O(n+e), where n is the number of nodes and e is the number of edges
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        nodeMap: Dict[int, Node] = {}

        def _clone(node: Node):
            if node.val in nodeMap:
                return nodeMap[node.val]

            nodeMap[node.val] = Node(node.val)
            newNode = nodeMap[node.val]

            for neighbor in node.neighbors:
                newNode.neighbors.append(_clone(neighbor))

            return newNode

        return _clone(node) if node else None


# Helper function to convert adjacency list to Node, time complexity: O(n+e), where n is the number of nodes and e is the number of edges
def adjListToNode(adjList: List[List[int]]) -> Optional[Node]:
    nodeMap: Dict[int, Node] = {}
    for val, neighbors in enumerate(adjList, 1):
        if val not in nodeMap:
            nodeMap[val] = Node(val)
        for neighbor in neighbors:
            if neighbor not in nodeMap:
                nodeMap[neighbor] = Node(neighbor)
            nodeMap[val].neighbors.append(nodeMap[neighbor])

    return nodeMap[1] if nodeMap else None


class Test(unittest.TestCase):
    def test1(self):
        adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
        node = adjListToNode(adjList)
        print(node)
        s = Solution()
        node2 = s.cloneGraph(node)
        self.assertEqual(node, node2)

    def test1(self):
        adjList = []
        node = adjListToNode(adjList)
        print(node)
        s = Solution()
        node2 = s.cloneGraph(node)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
