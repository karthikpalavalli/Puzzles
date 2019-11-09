from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_nums = Counter(nums)

        return not all([count == 1 for count in freq_nums.values()])
