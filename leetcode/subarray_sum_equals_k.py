from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_occurences_map = dict()

        sum_occurences_map[0] = 1
        current_sum = 0
        array_sum_count = 0

        for num in nums:
            current_sum += num

            if current_sum - k in sum_occurences_map.keys():
                array_sum_count += sum_occurences_map[current_sum - k]

            if current_sum not in sum_occurences_map.keys():
                sum_occurences_map[current_sum] = 0

            sum_occurences_map[current_sum] += 1

        return array_sum_count


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1]
    print(sol.subarraySum(nums, 2))