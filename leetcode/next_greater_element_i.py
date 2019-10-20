from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        position_map = {element: index for index, element in enumerate(nums2)}

        result_list = list()

        for val in nums1:
            next_greatest_right = -1

            for nums_2_idx in range(position_map[val] + 1, len(nums2)):
                if nums2[nums_2_idx] > val:
                    next_greatest_right = nums2[nums_2_idx]
                    break

            result_list.append(next_greatest_right)

        return result_list