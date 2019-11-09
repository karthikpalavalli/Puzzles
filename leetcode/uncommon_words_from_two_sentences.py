from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        word_list = A.split() + B.split()

        word_freq = Counter(word_list)

        return [key for key, value in word_freq.items() if value > 1]
