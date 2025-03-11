import unittest
from typing import List, Optional


class BrowserHistory:
    def __init__(self, homepage: str):
        self.history: List = [homepage]
        self.curr: int = 0

    # time complexity: O(self.curr), because list[:self.curr] is O(self.curr)
    def visit(self, url: str) -> None:
        self.curr += 1
        self.history = self.history[: self.curr]
        self.history.append(url)

    # time complexity: O(1)
    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    # time complexity: O(1)
    def forward(self, steps: int) -> Optional[str]:
        self.curr = min(self.curr + steps, len(self.history) - 1)
        return self.history[self.curr]


class Test(unittest.TestCase):
    def test1(self):
        obj = BrowserHistory("leetcode.com")
        obj.visit("google.com")
        obj.visit("facebook.com")
        obj.visit("youtube.com")
        self.assertEqual(obj.back(1), "facebook.com")
        self.assertEqual(obj.back(1), "google.com")
        self.assertEqual(obj.forward(1), "facebook.com")
        obj.visit("linkedin.com")
        self.assertEqual(obj.forward(2), "linkedin.com")
        self.assertEqual(obj.back(2), "google.com")
        self.assertEqual(obj.back(7), "leetcode.com")


if __name__ == "__main__":
    unittest.main()
