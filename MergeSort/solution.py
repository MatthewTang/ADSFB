import unittest
from typing import List, Optional


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}, {self.value})"


class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def _mergeSort(pairs):
            # base case
            if len(pairs) == 1:
                return pairs

            mid = len(pairs) // 2
            left = _mergeSort(pairs[:mid])
            right = _mergeSort(pairs[mid:])

            # merge sorted left and right
            merged = []
            lp = rp = 0
            while lp < len(left) or rp < len(right):
                if lp >= len(left):
                    merged += right[rp:]
                    return merged
                if rp >= len(right):
                    merged += left[lp:]
                    return merged
                if left[lp].key <= right[rp].key:
                    merged.append(left[lp])
                    lp += 1
                else:
                    merged.append(right[rp])
                    rp += 1
            return merged

        return _mergeSort(pairs)


class Test(unittest.TestCase):
    def test1(self):
        input_tuple = [
            (5, "apple"),
            (2, "banana"),
            (9, "cherry"),
            (1, "date"),
            (9, "elderberry"),
        ]
        expected_tuple = [
            (1, "date"),
            (2, "banana"),
            (5, "apple"),
            (9, "cherry"),
            (9, "elderberry"),
        ]
        pairs: List[Pair] = [Pair(p[0], p[1]) for p in input_tuple]
        expected_pairs: List[Pair] = [Pair(p[0], p[1]) for p in expected_tuple]
        s = Solution()
        result = s.mergeSort(pairs)
        print(result)
        self.assertEqual(str(result), str(expected_pairs))

    def test2(self):
        input_tuple = [(3, "cat"), (2, "dog"), (3, "bird")]
        expected_tuple = [(2, "dog"), (3, "cat"), (3, "bird")]
        pairs: List[Pair] = [Pair(p[0], p[1]) for p in input_tuple]
        expected_pairs: List[Pair] = [Pair(p[0], p[1]) for p in expected_tuple]
        s = Solution()
        result = s.mergeSort(pairs)
        print(result)
        self.assertEqual(str(result), str(expected_pairs))


if __name__ == "__main__":
    unittest.main()
