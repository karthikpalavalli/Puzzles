from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_to_swap = -1

        for idx in range(len(nums) - 1, 0, -1):
            if nums[idx - 1] < nums[idx]:
                idx_to_swap = idx - 1
                break

        if idx_to_swap == -1:
            nums.reverse()

        secondary_idx = idx_to_swap + 1
        for idx in range(idx_to_swap + 1, len(nums)):
            if nums[idx_to_swap] < nums[idx] < nums[secondary_idx]:
                secondary_idx = idx

        nums[idx_to_swap], nums[secondary_idx] = nums[secondary_idx], nums[idx_to_swap]

        end_entries = list(reversed(nums[idx_to_swap + 1:]))

        for idx in range(idx_to_swap + 1, len(nums)):
            nums[idx] = end_entries[idx - idx_to_swap - 1]
