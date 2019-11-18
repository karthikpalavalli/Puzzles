from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        elif len(nums) == 1:
            return nums[0]

        max_till_prev = nums[0]

        max_array = list()

        for idx, val in enumerate(nums):
            max_till_prev = max(max_till_prev, max_till_prev + val)

            max_array.append(max_till_prev)

        return max_till_prev[-1]
