class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = "".join([ch for ch in S.upper()[::-1] if ch != '-'])
        new_S = ""

        while len(S):
            if len(S) < K:
                new_S += S
                S = str()
                continue

            else:
                new_S += S[:K]
                S = S[K:]

                if len(S):
                    new_S += '-'
        return new_S[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.licenseKeyFormatting("5F3Z-2e-9-w", 4))
