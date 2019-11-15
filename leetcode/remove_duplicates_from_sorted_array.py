from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        ptr_unique = 0
        ptr_iter = 1

        while ptr_iter < len(nums):
            if nums[ptr_iter] != nums[ptr_unique]:
                ptr_unique += 1
                nums[ptr_unique] = nums[ptr_iter]

            ptr_iter += 1

        return ptr_unique
