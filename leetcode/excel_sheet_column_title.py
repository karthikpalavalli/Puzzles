class Solution:
    def convertToTitle(self, n: int) -> str:
        conversion_str = ""

        while n:
            rem = (n-1) % 26
            conversion_str = str(rem) + conversion_str
            n = (n-1) // 26

        title_str = ""

        for ch in conversion_str:
            title_str += chr(64 + int(ch))

        return title_str


if __name__ == "__main__":
    sol = Solution()
    sol.convertToTitle(28)