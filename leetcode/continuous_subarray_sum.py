from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = dict()

        current_sum = 0

        for idx in range(len(nums)):
            current_sum += nums[idx]

            remainder = current_sum % k

            if remainder in remainder_map.keys():
                if (idx - remainder_map[remainder]) >= 2:
                    return True

            remainder_map[remainder] = idx

        return False
