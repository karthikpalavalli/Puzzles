class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = len(str(N))
        sum = 0

        for ch in str(N):
            sum += int(ch) ** k

        if sum == N:
            return True

        return False
