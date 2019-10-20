from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency_map = Counter(s)

        for index, ch in enumerate(s):
            if frequency_map[ch] == 1:
                return index

        return -1
