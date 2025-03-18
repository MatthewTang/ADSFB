import unittest
from typing import List, Optional

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int, pick: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0



class Solution:
    # time: O(logn), space: O(1)
    def guessNumber(self, n: int, pick: int) -> int:
        l, r = 0, n
        while l <= r:
            m = (l+r) //2
            if guess(m, pick) < 0:
                r = m - 1
            elif guess(m, pick) > 0:
                l = m + 1
            else:
                return m

        return -1


class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        n = 10
        pick = 6
        result = s.guessNumber(n, pick)
        self.assertIs(result, 6)

    def test2(self):
        s = Solution()
        n = 1
        pick = 1
        result = s.guessNumber(n, pick)
        self.assertIs(result, 1)

    def test3(self):
        s = Solution()
        n = 2
        pick = 1
        result = s.guessNumber(n, pick)
        self.assertIs(result, 1)


if __name__ == "__main__":
    unittest.main()
