from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ord_dict = {letter: index for index, letter in enumerate(order)}

        for idx in range(0, len(words) - 1):
            for letter_idx in range(len(words[idx])):
                ord_1 = ord_dict[words[idx][letter_idx]]
                ord_2 = -1

                if letter_idx < len(words[idx + 1]):
                    ord_2 = ord_dict[words[idx + 1][letter_idx]]

                if ord_1 > ord_2:
                    return False

                if ord_1 < ord_2:
                    break

        return True


if __name__ == "__main__":
    word_list = ["hello", "leetcode"]
    word_order = "hlabcdefgijkmnopqrstuvwxyz"
    sol = Solution()
    print(sol.isAlienSorted(word_list, word_order))