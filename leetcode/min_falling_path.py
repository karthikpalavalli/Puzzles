class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dp_prev = [0] * len(A[0])

        iter_vals = reversed(range(len(A)))

        for i in iter_vals:
            dp_curr = [0] * len(A[0])

            for j in range(len(A[0])):
                min_next = dp_prev[j]

                if j > 0:
                    min_next = min(min_next, dp_prev[j - 1])

                if j < len(A[0]) - 1:
                    min_next = min(min_next, dp_prev[j + 1])

                dp_curr[j] = A[i][j] + min_next

            dp_prev = dp_curr

        return min(dp_prev)


if __name__ == "__main__":
    sol = Solution()
    k = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(sol.minFallingPathSum(k))