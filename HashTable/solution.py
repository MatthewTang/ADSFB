import unittest
from typing import Optional, List
from collections import deque


class Pair:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val


# open addressing
class HashTable:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.map: List[Optional[Pair]] = [None] * capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index].val = value
                return
            index += 1
            index % self.capacity

        self.map[index] = Pair(key, value)
        self.size += 1
        if self.size >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                return True

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        oldMap = self.map
        self.map = [None] * self.capacity
        self.size = 0
        for i in oldMap:
            if i:
                self.insert(i.key, i.val)

    def hash(self, key: int) -> int:
        return key % self.capacity


class Test(unittest.TestCase):
    def test1(self):
        hashTable = HashTable(4)
        self.assertIsNone(hashTable.insert(1, 2))
        self.assertIs(hashTable.get(1), 2)
        self.assertIsNone(hashTable.insert(1, 3))
        self.assertIs(hashTable.get(1), 3)
        self.assertTrue(hashTable.remove(1))
        self.assertIs(hashTable.get(1), -1)

    def test2(self):
        hashTable = HashTable(2)
        self.assertIs(hashTable.getCapacity(), 2)
        self.assertIsNone(hashTable.insert(6, 7))
        self.assertIs(hashTable.getCapacity(), 4)
        self.assertIsNone(hashTable.insert(1, 2))
        self.assertIs(hashTable.getCapacity(), 8)
        self.assertIsNone(hashTable.insert(3, 4))
        self.assertIs(hashTable.getCapacity(), 8)
        self.assertIs(hashTable.getSize(), 3)

    def test3(self):
        hashTable = HashTable(4)
        self.assertIsNone(hashTable.insert(1, 2))
        self.assertIs(hashTable.get(1), 2)
        self.assertIsNone(hashTable.insert(1, 3))
        self.assertIs(hashTable.get(1), 3)
        self.assertIs(hashTable.remove(1), True)
        self.assertIs(hashTable.get(1), -1)


if __name__ == "__main__":
    unittest.main()
