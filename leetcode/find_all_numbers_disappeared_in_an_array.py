from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1

            nums[idx] = nums[idx] * -1

        missing_numbers = list()

        for idx in range(len(nums)):
            if nums[idx] < 0:
                missing_numbers.append(idx + 1)

        return missing_numbers
