from typing import List
from collections import Counter
from operator import itemgetter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        word_freq = dict(Counter(paragraph.lower().split()))

        word_freq = sorted(word_freq.items(), key=itemgetter(1), reverse=True)

        for word, _ in word_freq:
            if word not in banned:
                return word


if __name__ == "__main__":
    test_s = "hello my name is hello"
    test_banned = list()

    sol = Solution()
    sol.mostCommonWord(test_s, test_banned)
