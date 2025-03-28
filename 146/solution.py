from collections import deque
import unittest
from typing import Dict, List, Optional


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

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: Dict[int : List[int]] = {}  # key -> [value, age]
        self.age = 0
        pass

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.age += 1
        value, _ = self.map[key]
        self.map[key] = [value, self.age]
        return value

    # O(c), where c is capacity
    def put(self, key: int, value: int) -> None:
        self.age += 1

        if key in self.map or len(self.map) < self.capacity:
            self.map[key] = [value, self.age]
            return

        leastRecent = sorted(self.map.items(), key=lambda x: x[1][1])[0][0]

        del self.map[leastRecent]
        self.map[key] = [value, self.age]


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
