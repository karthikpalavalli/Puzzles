from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_freq = Counter(list(magazine))

        for letter in ransomNote:
            letter_freq[letter] = letter_freq[letter] - 1

        letters_not_found = list(filter(lambda x: x < 0, letter_freq.values()))

        if letters_not_found:
            return False

        return True


if __name__ == "__main__":
    sol = Solution()
    test_magazine = "aabcd"
    test_ransom_note = "aa"

    print(sol.canConstruct(test_ransom_note, test_magazine))