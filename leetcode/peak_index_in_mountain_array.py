from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        low = 0
        high = len(A) - 1
        result = 0

        while low <= high:
            mid = (low + high) // 2

            if A[mid - 1] < A[mid] > A[mid + 1]:
                result = mid
                break

            elif A[mid - 1] < A[mid] < A[mid + 1]:
                low = mid + 1

            else:
                high = mid - 1

        return result
