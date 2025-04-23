import unittest
from typing import List, Optional
from functools import lru_cache


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

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     def dfs(i: int, j: int) -> int:
    #         if i == len(text1) or j == len(text2):
    #             return 0
    #
    #         if text1[i] == text2[j]:
    #             return 1 + dfs(i + 1, j + 1)
    #
    #         return max(dfs(i + 1, j), dfs(i, j + 1))
    #
    #     return dfs(0, 0)

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     @lru_cache
    #     def dfs(i: int, j: int) -> int:
    #         if i == len(text1) or j == len(text2):
    #             return 0
    #
    #         if text1[i] == text2[j]:
    #             return 1 + dfs(i + 1, j + 1)
    #
    #         return max(dfs(i + 1, j), dfs(i, j + 1))
    #
    #     return dfs(0, 0)

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     l1, l2 = len(text1), len(text2)
    #     cache = [[0] * l2 for _ in range(l1)]
    #     def dfs(i: int, j: int) -> int:
    #         if i == len(text1) or j == len(text2):
    #             return 0
    #         if cache[i][j]:
    #             return cache[i][j]
    #
    #         if text1[i] == text2[j]:
    #             o = 1 + dfs(i + 1, j + 1)
    #             cache[i][j] = o
    #             return o
    #
    #
    #         o = max(dfs(i + 1, j), dfs(i, j + 1))
    #         cache[i][j] = o
    #         return o
    #
    #     return dfs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        prev = [0] * l1
        for i in range(l2 - 1, -1, -1):
            curr = [0] * l1
            for j in range(l1 - 1, -1, -1):
                if text1[j] == text2[i]:
                    curr[j] = (
                        1 if j == l1 - 1 else max(curr[j + 1], prev[j + 1] + 1, prev[j])
                    )
                else:
                    curr[j] = prev[j] if j == l1 - 1 else max(curr[j + 1], prev[j])
            prev = curr

        return max(prev)


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
        text2 = "aa"
        text1 = "a"
        expected = 1
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
        self.assertEqual(result, expected)

    def test6(self):
        s = Solution()
        text1 = "fcvafurqjylclorwfoladwfqzkbebslwnmpmlkbezkxoncvwhstwzwpqxqtyxozkpgtgtsjobujezgrkvevklmludgtyrmjaxyputqbyxqvupojutsjwlwluzsbmvyxifqtglwvcnkfsfglwjwrmtyxmdgjifyjwrsnenuvsdedsbqdovwzsdghclcdexmtsbexwrszihcpibwpidixmpmxshwzmjgtadmtkxqfkrsdqjcrmxkbkfoncrcvoxuvcdytajgfwrcxivixanuzerebuzklyhezevonqdsrkzetsrgfgxibqpmfuxcrinetyzkvudghgrytsvwzkjulmhanankxqfihenuhmfsfkfepibkjmzybmlkzozmluvybyzsleludsxkpinizoraxonmhwtkfkhudizepyzijafqlepcbihofepmjqtgrsxorunshgpazovuhktatmlcfklafivivefyfubunszyvarcrkpsnglkduzaxqrerkvcnmrurkhkpargvcxefovwtapedaluhclmzynebczodwropwdenqxmrutuhehadyfspcpuxyzodifqdqzgbwhodcjonypyjwbwxepcpujerkrelunstebopkncdazexsbezmhynizsvarafwfmnclerafejgnizcbsrcvcnwrolofyzulcxaxqjqzunedidulspslebifinqrchyvapkzmzwbwjgbyrqhqpolwjijmzyduzerqnadapudmrazmzadstozytonuzarizszubkzkhenaxivytmjqjgvgzwpgxefatetoncjgjsdilmvgtgpgbibexwnexstipkjylalqnupexytkradwxmlmhsnmzuxcdkfkxyfgrmfqtajatgjctenqhkvyrgvapctqtyrufcdobibizihuhsrsterozotytubefutaxcjarknynetipehoduxyjstufwvkvwvwnuletybmrczgtmxctuny"
        text2 = "nohgdazargvalupetizezqpklktojqtqdivcpsfgjopaxwbkvujilqbclehulatshehmjqhyfkpcfwxovajkvankjkvevgdovazmbgtqfwvejczsnmbchkdibstklkxarwjqbqxwvixavkhylqvghqpifijohudenozotejoxavkfkzcdqnoxydynavwdylwhatslyrwlejwdwrmpevmtwpahatwlaxmjmdgrebmfyngdcbmbgjcvqpcbadujkxaxujudmbejcrevuvcdobolcbstifedcvmngnqhudixgzktcdqngxmruhcxqxypwhahobudelivgvynefkjqdyvalmvudcdivmhghqrelurodwdsvuzmjixgdexonwjczghalsjopixsrwjixuzmjgxydqnipelgrivkzkxgjchibgnqbknstspujwdydszohqjsfuzstyjgnwhsrebmlwzkzijgnmnczmrehspihspyfedabotwvwxwpspypctizyhcxypqzctwlspszonsrmnyvmhsvqtkbyhmhwjmvazaviruzqxmbczaxmtqjexmdudypovkjklynktahupanujylylgrajozobsbwpwtohkfsxeverqxylwdwtojoxydepybavwhgdehafurqtcxqhuhkdwxkdojipolctcvcrsvczcxedglgrejerqdgrsvsxgjodajatsnixutihwpivihadqdotsvyrkxehodybapwlsjexixgponcxifijchejoxgxebmbclczqvkfuzgxsbshqvgfcraxytaxeviryhexmvqjybizivyjanwxmpojgxgbyhcruvqpafwjslkbohqlknkdqjixsfsdurgbsvclmrcrcnulinqvcdqhcvwdaxgvafwravunurqvizqtozuxinytafopmhchmxsxgfanetmdcjalmrolejidylkjktunqhkxchyjmpkvsfgnybsjedmzkrkhwryzan"
        expected = 323
        result = s.longestCommonSubsequence(text1, text2)
        self.assertEqual(result, expected)

    def test7(self):
        s = Solution()
        text1 = "abab"
        text2 = "baab"
        expected = 3
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)

    def test8(self):
        s = Solution()
        text1 = "bsbininm"
        text2 = "jmjkbkjkv"
        expected = 1
        result = s.longestCommonSubsequence(text1, text2)
        self.assertIs(result, expected)


if __name__ == "__main__":
    unittest.main()
