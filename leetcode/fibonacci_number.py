class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0

        if N == 1:
            return 1

        first = 0
        second = 1

        for i in range(N):
            total = first + second
            first = second
            second = total

        return total


if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(3))
