from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        grouped_dict = defaultdict(list)

        for string in strings:
            pattern = str()

            if len(string) == 1:
                grouped_dict["NA"].append(string)
                continue

            for idx in range(1, len(string)):
                pattern += str((ord(string[idx]) - ord(string[idx - 1])) % 26)

            grouped_dict[pattern].append(string)

        return list(grouped_dict.values())