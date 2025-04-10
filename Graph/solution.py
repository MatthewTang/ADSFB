import unittest
from typing import Dict, List, Optional
from collections import deque


class GraphNode:
    def __init__(self, val: int, neighbours: List[int] = []) -> None:
        self.val = val
        self.neighbours = neighbours

    def addNeighbour(self, val: int) -> None:
        if not val in self.neighbours:
            self.neighbours.append(val)

    def removeNeighbour(self, val: int) -> bool:
        if not val in self.neighbours:
            return False

        self.neighbours.remove(val)
        return True

    def hasNeighbour(self, val: int) -> bool:
        return val in self.neighbours


class Graph:
    def __init__(self) -> None:
        self.nodes: Dict[int, GraphNode] = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src in self.nodes:
            self.nodes[src].addNeighbour(dst)
        else:
            n = GraphNode(src, [dst])
            self.nodes[src] = n

        if not dst in self.nodes:
            n = GraphNode(dst, [])
            self.nodes[dst] = n

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.nodes:
            return self.nodes[src].removeNeighbour(dst)
        else:
            return False

    def hasPath(self, src: int, dst: int) -> bool:
        if src in self.nodes and dst in self.nodes:
            # return self.dfs(src, dst, [])
            return self.bfs(src, dst)
        else:
            return False

    def dfs(self, src: int, target: int, visited: List[int]) -> bool:
        curr = self.nodes[src]
        if curr.val == target:
            return True
        if curr.val in visited:
            return False
        if len(curr.neighbours) == 0:
            return False

        visited.append(curr.val)
        for n in curr.neighbours:
            if self.dfs(n, target, visited):
                return True
        visited.remove(curr.val)
        return False

    def bfs(self, src: int, target: int) -> bool:
        q = deque([src])
        visited = set()

        while len(q):
            for _ in range(len(q)):
                v = q.popleft()
                if v == target:
                    return True
                visited.add(v)
                curr = self.nodes[v]
                for n in curr.neighbours:
                    if n not in visited:
                        q.append(n)
        return False


class Test(unittest.TestCase):
    def test1(self):
        g = Graph()
        g.addEdge(1, 2)
        g.addEdge(2, 3)
        self.assertEqual(g.hasPath(1, 3), True)
        self.assertEqual(g.hasPath(3, 1), False)
        self.assertEqual(g.removeEdge(1, 2), True)
        self.assertEqual(g.hasPath(1, 3), False)

    def test2(self):
        g = Graph()
        g.addEdge(1, 2)
        g.addEdge(2, 3)
        g.addEdge(3, 1)
        self.assertEqual(g.hasPath(1, 3), True)
        self.assertEqual(g.hasPath(3, 1), True)


if __name__ == "__main__":
    unittest.main()
