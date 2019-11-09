class Solution:
    def titleToNumber(self, s: str) -> int:
        col_no = 0
        for idx, ch in enumerate(reversed(s)):
            col_no += (ord(ch) - ord("A") + 1) * (26 ** idx)

        return col_no


if __name__ == "__main__":
    sol = Solution()
    print(sol.titleToNumber("AZ"))