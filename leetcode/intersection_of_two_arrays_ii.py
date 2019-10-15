from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_dict = defaultdict(int)

        for num in nums1:
            intersection_dict[num] += 1

        intersection_list = list()

        for num in nums2:
            if intersection_dict[num] != 0:
                intersection_list.append(num)
                intersection_dict[num] -= 1

        return intersection_list


if __name__ == "__main__":
    sol = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]

    print(sol.intersect(nums1, nums2))