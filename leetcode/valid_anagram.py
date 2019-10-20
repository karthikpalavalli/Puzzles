from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_map = Counter(s)

        for letter in t:
            if letter not in frequency_map.keys():
                return False

            frequency_map[letter] -= 1

        return all(ele == 0 for ele in frequency_map.values())


if __name__ == "__main__":
    str_1 = "anagram"
    str_2 = "nagaram"

    sol = Solution()
    print(sol.isAnagram(str_1, str_2))