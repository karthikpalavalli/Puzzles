from typing import List
import heapq


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        my_heap = nums[:3]
        heapq.heapify(my_heap)

        if len(nums) > 3:
            for idx in range(3, len(nums)):
                smallest_heap_element = heapq.heappop(my_heap)

                if nums[idx] > smallest_heap_element:
                    smallest_heap_element = nums[idx]

                heapq.heappush(my_heap, smallest_heap_element)

        prod = 1
        for ele in my_heap:
            prod *= ele

        return prod
