class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = list()

        word = ""

        for i in range(len(s)):
            if s[i] != ' ':
                word += s[i]

            else:
                if word:
                    word_list.append(word)

                word = ""

        if word:
            word_list.append(word)

        reversed_string = ""
        for i in range(len(word_list)):
            reversed_string = word_list[i] + " " + reversed_string

        return reversed_string[:-1]


if __name__ == "__main__":
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))
