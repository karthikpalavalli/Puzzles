class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num // 2

        while low <= high:
            mid = (low + high) // 2

            mid_2 = mid ** 2

            if mid_2 == num:
                return True

            elif mid_2 < num:
                low = mid + 1

            else:
                high = mid - 1

        return False
