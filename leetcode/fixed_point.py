class Solution:
    @staticmethod
    def binary_search(A, low, high):
        while high > low:
            mid = (high + low) // 2

            if A[mid] == mid:
                return mid

            elif A[mid] > mid:
                high = mid - 1

            else:
                low = mid + 1

        return -1

    def fixedPoint(self, A):
        fixed_point_index = self.binary_search(A, 0, len(A) - 1)

        if fixed_point_index == -1:
            return fixed_point_index

        else:
            while A[fixed_point_index - 1] == fixed_point_index - 1:
                fixed_point_index -= 1

            return fixed_point_index