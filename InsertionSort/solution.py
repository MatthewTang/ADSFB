import unittest
from typing import List, Optional


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, {self.value})"


class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = [pairs[:]]
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            res.append(pairs[:])
        return res


class Test(unittest.TestCase):
    def test1(self):
        input_tuple = [(5, "apple"), (2, "banana"), (9, "cherry")]
        expected = [
            [(5, "apple"), (2, "banana"), (9, "cherry")],
            [(2, "banana"), (5, "apple"), (9, "cherry")],
            [(2, "banana"), (5, "apple"), (9, "cherry")],
        ]
        pairs: List[Pair] = [Pair(p[0], p[1]) for p in input_tuple]
        expected_pairs: List[List[Pair]] = [
            [Pair(p[0], p[1]) for p in pairs] for pairs in expected
        ]
        s = Solution()
        result = s.insertionSort(pairs)
        self.assertEqual(str(result), str(expected_pairs))

    def test2(self):
        input_tuple = [(3, "cat"), (3, "bird"), (2, "dog")]
        expected = [
            [(3, "cat"), (3, "bird"), (2, "dog")],
            [(3, "cat"), (3, "bird"), (2, "dog")],
            [(2, "dog"), (3, "cat"), (3, "bird")],
        ]
        pairs: List[Pair] = [Pair(p[0], p[1]) for p in input_tuple]
        expected_pairs: List[List[Pair]] = [
            [Pair(p[0], p[1]) for p in pairs] for pairs in expected
        ]
        s = Solution()
        result = s.insertionSort(pairs)
        self.assertEqual(str(result), str(expected_pairs))


if __name__ == "__main__":
    unittest.main()
