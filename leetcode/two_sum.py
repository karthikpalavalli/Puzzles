class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_to_loc = dict()

        for iter in range(len(nums)):
            compliment_val = target - nums[iter]

            if value_to_loc.get(compliment_val, -1) != -1:
                return [value_to_loc[compliment_val], iter]

            value_to_loc[nums[iter]] = iter


