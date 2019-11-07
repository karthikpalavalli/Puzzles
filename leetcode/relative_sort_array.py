from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq_arr1 = Counter(arr1)

        result_arr = list()

        for ele in arr2:
            result_arr.extend([ele] * freq_arr1[ele])

        remaining_elements = set(arr1) - set(arr2)

        for ele in sorted(remaining_elements):
            result_arr.extend([ele] * freq_arr1[ele])

        return result_arr
