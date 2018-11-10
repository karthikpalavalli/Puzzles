class Solution:
    def removeVowels(self, S) -> str:
        return ''.join(filter(lambda s: s not in ['a', 'e', 'i', 'o', 'u'], list(S)))