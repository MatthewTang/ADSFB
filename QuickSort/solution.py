import unittest
from typing import List, Optional


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, {self.value})"


class Solution:
    # time complexity: O(nlogn) in general, O(n^2) in worst case, space complexity: O(logn) in general, O(n) in worst case
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def _quickSort(pairs, s, e):
            if e <= s:
                return

            p = pairs[e]
            l = i = s
            while i < e:
                if pairs[i].key < p.key:
                    pairs[i], pairs[l] = pairs[l], pairs[i]
                    l += 1
                    i += 1
                else:
                    i += 1
            pairs[l], pairs[e] = pairs[e], pairs[l]

            _quickSort(pairs, s, l - 1)
            _quickSort(pairs, l + 1, e)

            return

        if len(pairs) > 1:
            _quickSort(pairs, 0, len(pairs) - 1)

        return pairs


class Test(unittest.TestCase):
    def test1(self):
        input_tuple = [
            (5, "apple"),
            (9, "banana"),
            (9, "cherry"),
            (1, "date"),
            (9, "elderberry"),
        ]
        expected_tuple = [
            (1, "date"),
            (5, "apple"),
            (9, "elderberry"),
            (9, "cherry"),
            (9, "banana"),
        ]
        pairs: List[Pair] = [Pair(p[0], p[1]) for p in input_tuple]
        expected_pairs: List[Pair] = [Pair(p[0], p[1]) for p in expected_tuple]
        s = Solution()
        result = s.quickSort(pairs)
        self.assertEqual(str(result), str(expected_pairs))

    def test2(self):
        input_tuple = [(3, "cat"), (2, "dog"), (3, "bird")]
        expected_tuple = [(2, "dog"), (3, "bird"), (3, "cat")]
        pairs: List[Pair] = [Pair(p[0], p[1]) for p in input_tuple]
        expected_pairs: List[Pair] = [Pair(p[0], p[1]) for p in expected_tuple]
        s = Solution()
        result = s.quickSort(pairs)
        self.assertEqual(str(result), str(expected_pairs))

    def test3(self):
        input_tuple = []
        expected_tuple = []
        pairs: List[Pair] = [Pair(p[0], p[1]) for p in input_tuple]
        expected_pairs: List[Pair] = [Pair(p[0], p[1]) for p in expected_tuple]
        s = Solution()
        result = s.quickSort(pairs)
        self.assertEqual(str(result), str(expected_pairs))

    def test4(self):
        input_tuple = [(3, "cat")]
        expected_tuple = [(3, "cat")]
        pairs: List[Pair] = [Pair(p[0], p[1]) for p in input_tuple]
        expected_pairs: List[Pair] = [Pair(p[0], p[1]) for p in expected_tuple]
        s = Solution()
        result = s.quickSort(pairs)
        self.assertEqual(str(result), str(expected_pairs))


if __name__ == "__main__":
    unittest.main()
