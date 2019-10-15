from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_map = dict(Counter(nums1))

        intersection_set = set()

        for num in nums2:
            if num in num1_map and num not in intersection_set:
                intersection_set.add(num)

        return list(intersection_set)
