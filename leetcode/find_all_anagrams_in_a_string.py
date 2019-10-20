from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter_map = Counter(p)

        if len(s) < len(p):
            return []

        if len(s) == len(p) and Counter(s) == Counter(p):
            return [0]

        s_counter_map = Counter([])
        result_list = list()

        for current_idx in range(len(s)):
            s_counter_map[s[current_idx]] += 1

            if current_idx >= len(p):
                s_counter_map[s[current_idx - len(p)]] -= 1

            if s_counter_map[s[current_idx - len(p)]] == 0:
                del s_counter_map[s[current_idx - len(p)]]

            if s_counter_map == p_counter_map:
                result_list.append(current_idx - len(p) + 1)

        return result_list


if __name__ == "__main__":
    s_1 = "cbaebabacd"
    s_2 = "abc"

    sol = Solution()
    print(sol.findAnagrams(s_1, s_2))