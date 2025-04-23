import unittest
from typing import List, Optional


class Solution:
    # # dfs (list): O(2^(m+n))
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     def dfs(text: str):
    #         if len(text)  == 0:
    #             return []
    #
    #         c = text[0]
    #         _ss = [c]
    #         ss = dfs(text[1:])
    #         for s in ss:
    #             _ss.append(s)
    #             _ss.append(c + s)
    #         return _ss
    #
    #     ss1 = dfs(text1)
    #     ss2 = dfs(text2)
    #
    #     res = 0
    #     for s in ss1:
    #         if s in ss2:
    #             res = max(res, len(s))
    #
    #     return res
    #
    # # dfs (map): O(n * 2^n + m * 2^m)
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     def dfs(text: str):
    #         if len(text) == 0:
    #             return {}
    #
    #         c = text[0]
    #         _ss = {c: 1}
    #         ss = dfs(text[1:])
    #         for s in ss:
    #             _ss[s] = 1
    #             _ss[c + s] = 1
    #         return _ss
    #
    #     ss1 = dfs(text1)
    #     ss2 = dfs(text2)
    #
    #     res = 0
    #     for s in ss1:
    #         if s in ss2:
    #             res = max(res, len(s))
    #
    #     return res

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return


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

    def test4(self):
        s = Solution()
        text1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        text2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        expected = 210
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)

    def test5(self):
        s = Solution()
        text1 = "yzebsbuxmtcfmtodclszgh"
        text2 = "ejevmhcvshclydqrulwbyha"
        expected = 6
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
