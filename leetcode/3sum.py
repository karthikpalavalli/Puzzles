import math


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        possible_sols = set()

        print(nums)
        split_val = int(math.ceil(len(nums)/2))
        print(split_val)

        val_to_loc = {nums[i]: i for i in range(split_val, len(nums))}

        if len(nums) < 3:
            return []

        for pivot_index in range(1, int(math.ceil(len(nums)/2))):
            for l_iter in range(pivot_index-1, -1, -1):
                target_val = 0 - (nums[pivot_index] + nums[l_iter])

                if target_val in val_to_loc:
                    possible_sols.add((nums[l_iter], nums[pivot_index], target_val))

        possible_sols = map(list, possible_sols)

        return list(possible_sols)


if __name__=="__main__":
    sol = Solution()

    print(sol.threeSum([1, 2, -2, -1]))