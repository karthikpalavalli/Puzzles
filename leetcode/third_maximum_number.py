from typing import List
import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return 0

        distinct_elements = list(set(nums))

        if len(distinct_elements) < 3:
            return max(distinct_elements)

        my_min_heap = distinct_elements[:3]

        heapq.heapify(my_min_heap)

        if len(distinct_elements) > 3:
            for num in distinct_elements[3:]:
                heap_element = heapq.heappop(my_min_heap)

                if num > heap_element:
                    heap_element = num

                heapq.heappush(my_min_heap, heap_element)

        result = heapq.nlargest(3, my_min_heap)

        return result[-1]