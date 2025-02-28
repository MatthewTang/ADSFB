import unittest
from typing import List


class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity


class Test(unittest.TestCase):
    def test1(self):
        da = DynamicArray(1)
        self.assertEqual(da.getSize(), 0)
        self.assertEqual(da.getCapacity(), 1)
        print(da.array)

    def test2(self):
        da = DynamicArray(1)
        da.pushback(1)
        self.assertEqual(da.getCapacity(), 1)
        da.pushback(2)
        self.assertEqual(da.getCapacity(), 2)
        print(da.array)

    def test3(self):
        da = DynamicArray(1)
        self.assertEqual(da.getSize(), 0)
        self.assertEqual(da.getCapacity(), 1)
        da.pushback(1)
        self.assertEqual(da.getSize(), 1)
        self.assertEqual(da.getCapacity(), 1)
        da.pushback(2)
        self.assertEqual(da.getSize(), 2)
        self.assertEqual(da.getCapacity(), 2)
        self.assertEqual(da.get(1), 2)
        da.set(1, 3)
        self.assertEqual(da.get(1), 3)
        self.assertEqual(da.popback(), 3)
        self.assertEqual(da.getSize(), 1)
        self.assertEqual(da.getCapacity(), 2)
        print(da.array)


if __name__ == "__main__":
    unittest.main()
