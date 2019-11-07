from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search():
            nonlocal direction_flag

            low = 0
            high = len(nums)

            while low < high:
                mid = low + high // 2

                if nums[mid] > target or (direction_flag and nums[mid] == target):
                    high = mid - 1

                else:
                    low = mid + 1

            return mid

        range_vals = [-1, -1]

        direction_flag = True
        range_vals[0] = binary_search()
        direction_flag = False
        range_vals[1] = binary_search()

        return range_vals
