import unittest
from typing import List, Optional


class Solution:
    # assume finite n values
    def bucketSort(self, arr: List[int], n: int = 0) -> List[int]:
        if n <= 1:
            return arr

        record = [0] * n
        for i in arr:
            record[i] += 1

        i = 0

        # for j, k in enumerate(record):
        #     for _ in range(k):
        #         arr[i] = j
        #         i += 1

        for j in range(len(record)):
            for _ in range(record[j]):
                arr[i] = j
                i += 1

        return arr


class Test(unittest.TestCase):
    def test1(self):
        arr = [2, 2, 0, 1, 2, 1, 0]
        expected = [0, 0, 1, 1, 2, 2, 2]
        s = Solution()
        result = s.bucketSort(arr, 3)
        print(result)
        self.assertEqual(result, expected)

    def test2(self):
        arr = [2, 2, 0, 1, 2, 1, 0]
        expected = [0, 0, 1, 1, 2, 2, 2]
        s = Solution()
        result = s.bucketSort(arr, 3)
        print(result)
        self.assertEqual(result, expected)

    def test3(self):
        arr = []
        expected = []
        s = Solution()
        result = s.bucketSort(arr)
        self.assertEqual(result, expected)

    def test4(self):
        arr = [1]
        expected = [1]
        s = Solution()
        result = s.bucketSort(arr, 1)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
