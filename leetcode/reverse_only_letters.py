class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        alphabets = list(filter(lambda x: x.isalpha(), list(S)))

        result_str = str()

        for idx, ch in enumerate(S):
            if not ch.isalpha():
                result_str += ch

            else:
                result_str += alphabets.pop()

        return result_str


if __name__ == "__main__":
    sol = Solution()
    test_S = "ABC123"
    print(sol.reverseOnlyLetters(test_S))

