class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        new_string = ' '.join([word[::-1] for word in word_list])
        return new_string
