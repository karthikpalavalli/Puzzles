from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increasing = True
        decreasing = True

        for idx in range(0, len(A) - 1):
            if A[idx + 1] < A[idx]:
                increasing = False

            if A[idx + 1] > A[idx]:
                decreasing = False

        return increasing or decreasing