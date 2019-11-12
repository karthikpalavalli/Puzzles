from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        array_sum = sum(nums)

        left_sum = 0
        pivot_idx = -1

        for idx in range(1, len(nums) - 1):
            left_sum = left_sum + nums[idx - 1]

            right_sum = array_sum - left_sum - nums[idx]

            if left_sum == right_sum:
                pivot_idx = idx

        return pivot_idx
