from collections import OrderedDict
import unittest
from typing import Dict, List, Optional, OrderedDict


# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.map: Dict[int : List[int]] = {}  # key -> [value, age]
#         self.age = 0
#         pass
#
#     def get(self, key: int) -> int:
#         if key not in self.map:
#             return -1
#         self.age += 1
#         value, _ = self.map[key]
#         self.map[key] = [value, self.age]
#         return value
#
#     # O(c), where c is capacity
#     def put(self, key: int, value: int) -> None:
#         self.age += 1
#
#         if key in self.map or len(self.map) < self.capacity:
#             self.map[key] = [value, self.age]
#             return
#
#         # leastRecent = None
#         # minAge = self.age
#         # for k in self.map.keys():  # O(c)
#         #     _, age = self.map[k]
#         #     if age < minAge:
#         #         leastRecent = k
#         #         minAge = age
#         leastRecent = sorted(self.map.items(), key=lambda x: x[1][1])[0][0]
#
#         del self.map[leastRecent]
#         self.map[key] = [value, self.age]


# class Node:
#     def __init__(
#         self, val: int, prev: Optional["Node"] = None, next: Optional["Node"] = None
#     ) -> None:
#         self.val: int = val  # key
#         self.prev: Optional[Node] = prev
#         self.next: Optional[Node] = next
#
#
# # space: O(n)
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.map1: Dict[int:int] = {}  # key -> value
#         self.map2: Dict[int:Node] = {}  # key -> Node
#         self.head = Node(0)  # easier for add/remove first
#         self.tail = Node(0)
#         self.head.next = self.tail
#         self.tail.prev = self.head
#
#     # O(1)
#     def remove(self, node: Node):
#         node.prev.next = node.next
#         node.next.prev = node.prev
#
#     # O(1)
#     def insert(self, node: Node):
#         node.prev = self.tail.prev
#         node.next = self.tail
#         self.tail.prev.next = node
#         self.tail.prev = node
#
#     # O(1)
#     def get(self, key: int) -> int:
#         if key not in self.map1:
#             return -1
#         node: Node = self.map2[key]
#         self.remove(node)
#         self.insert(node)
#         return self.map1[key]
#
#     # O(1)
#     def put(self, key: int, value: int) -> None:
#
#         if key in self.map1:
#             node: Node = self.map2[key]
#             self.remove(node)
#             self.insert(node)
#             self.map1[key] = value
#             return
#
#         if len(self.map1) < self.capacity:
#             self.map1[key] = value
#             node = Node(key)
#             self.insert(node)
#             self.map2[key] = node
#             return
#
#         self.map1[key] = value
#         node = Node(key)
#         self.insert(node)
#         self.map2[key] = node
#
#         head: Node = self.head.next
#         del self.map1[head.val]
#         self.remove(head)


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache: OrderedDict = OrderedDict()  # using doubly-linked list w hash table
        self.capacity = capacity
        pass

    def get(self, key: int) -> int:
        if key not in self.cache:  # O(1)
            return -1
        self.cache.move_to_end(key)  # O(1)
        return self.cache[key]  # O(1)

    def put(self, key: int, val: int) -> None:
        if key in self.cache:  # O(1)
            self.cache.move_to_end(key)  # O(1)
        self.cache[key] = val  # O(1)

        if len(self.cache) > self.capacity:
            self.cache.popitem(False)  # O(1)

        return


class Test(unittest.TestCase):
    def test1(self):
        lRUCache = LRUCache(2)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        self.assertIs(lRUCache.get(1), 1)
        lRUCache.put(3, 3)
        self.assertIs(lRUCache.get(2), -1)
        lRUCache.put(4, 4)
        self.assertIs(lRUCache.get(1), -1)
        self.assertIs(lRUCache.get(3), 3)
        self.assertIs(lRUCache.get(4), 4)

    def test2(self):
        lRUCache = LRUCache(2)
        self.assertIs(lRUCache.get(2), -1)
        lRUCache.put(2, 6)
        self.assertIs(lRUCache.get(1), -1)
        lRUCache.put(1, 5)
        lRUCache.put(1, 2)
        self.assertIs(lRUCache.get(2), 6)
        self.assertIs(lRUCache.get(1), 2)

    def test3(self):
        lRUCache = LRUCache(3)
        lRUCache.put(1, 1)
        lRUCache.put(2, 2)
        lRUCache.put(3, 3)
        self.assertIs(lRUCache.get(2), 2)
        lRUCache.put(4, 4)
        lRUCache.put(5, 5)
        self.assertIs(lRUCache.get(2), 2)
        self.assertIs(lRUCache.get(3), -1)
        self.assertIs(lRUCache.get(1), -1)


if __name__ == "__main__":
    unittest.main()
