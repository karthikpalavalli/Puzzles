from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_new = {letter: index for index, letter in enumerate(order)}

        max_length = max([len(word) for word in words])

        for char_idx in range(max_length):
            for idx in range(len(words) - 1):
                ch_a = -1
                ch_b = -1

                if len(words[idx]) > char_idx:
                    ch_a = ord_new[words[idx][char_idx]]

                if len(words[idx + 1]) > char_idx:
                    ch_b = ord_new[words[idx + 1][char_idx]]

                if ch_a > ch_b:
                    return False

        return True


if __name__ == "__main__":
    sol = Solution()

    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"

    print(sol.isAlienSorted(words, order))
