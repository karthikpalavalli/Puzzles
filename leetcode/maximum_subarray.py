class Solution:
    def maxSubArray(self, nums):
        if not nums:
            return 0

        max_prev = nums[0]

        total_max = nums[0]

        for idx in range(1, len(nums)):
            max_prev = max(nums[idx], nums[idx] + max_prev)

            if max_prev > total_max:
                total_max = max_prev

        return total_max
