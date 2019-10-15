from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        if len(nums) == 1:
            return nums[0]

        elif 1 < len(nums) < 3:
            return -1

        for idx in range(1, len(nums) - 1, 2):
            if nums[idx - 1] == nums[idx] == nums[idx + 1]:
                continue
