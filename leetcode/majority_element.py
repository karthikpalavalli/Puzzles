from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_freq = Counter(nums)

        for key, value in nums_freq.items():
            if value > len(nums) // 2:
                return key
