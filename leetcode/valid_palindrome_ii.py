class Solution:
    def check_plaindrome_in_range(self, complete_string, start, end):
        valid = True

        print("Entered")
        print(start, end)

        while start < end:
            print("Inside the function: ", complete_string[start], complete_string[end])
            if complete_string[start] != complete_string[end]:
                valid = False
                break

            start += 1
            end -= 1

        return valid

    def validPalindrome(self, s: str) -> bool:
        palindrome = True

        for idx in range(0, len(s)//2):
            print(s[idx], s[~idx])
            if s[idx] != s[~idx]:
                palindrome = self.check_plaindrome_in_range(s, idx + 1, len(s) - idx - 1) or \
                             self.check_plaindrome_in_range(s, idx, len(s) - idx - 2)

        return palindrome


if __name__ == "__main__":
    sol = Solution()
    test_str = "abc"
    print(sol.validPalindrome(test_str))
