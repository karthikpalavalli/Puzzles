from typing import List


class Solution:
    def reverseList(self, s):
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp

        return s

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = self.reverseList(s)
        print(s)

        start_index = 0

        for i in range(len(s)):
            if s[i] == ' ':
                s[start_index:i] = s[start_index:i][::-1]
                start_index = i + 1

        s[start_index:len(s)] = s[start_index:len(s)][::-1]
        print(s)


if __name__ == "__main__":
    sol = Solution()
    words_list = list("the sky is blue")
    sol.reverseWords(words_list)
