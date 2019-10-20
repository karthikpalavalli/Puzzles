from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros_before_me = 0

        for idx in range(0, len(nums)):
            if nums[idx] != 0:
                temp = nums[idx]
                nums[idx] = nums[zeros_before_me]
                nums[zeros_before_me] = temp

                zeros_before_me += 1
