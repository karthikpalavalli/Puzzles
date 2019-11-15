class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        for idx in range(len(haystack) - len(needle)):
            if haystack[idx] == needle[0] and haystack[idx:idx+len(needle)] == needle:
                return idx

        return -1
