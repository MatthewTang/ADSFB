import unittest
from typing import List, Optional


class Solution:
    # dfs, time: O(n * 2^n) + O(m * 2^m) + O(2^(n+m)) = O(2^(n+m))
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dfs(text: str, i: int, res: List[str]):
            l = len(text)
            if i >= l:
                return
            c = text[i]
            _res = [c]
            for r in res:  # O(2^i)
                _res.append(r + c)  # O(i)
            res += _res  # O(2^i)
            dfs(text, i + 1, res)

        res1 = []
        dfs(text1, 0, res1)  # O(n * 2^n)

        res2 = []
        dfs(text2, 0, res2)  # O(m * 2^m)

        res = 0
        # O(2^n * 2^m) = O(2^(n+m))
        for r in res1:
            if r in res2:
                res = max(res, len(r))

        return res


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        text1 = "abcde"
        text2 = "ace"
        expected = 3
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)

    def test2(self):
        s = Solution()
        text1 = "abc"
        text2 = "abc"
        expected = 3
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)

    def test3(self):
        s = Solution()
        text1 = "abc"
        text2 = "def"
        expected = 0
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
