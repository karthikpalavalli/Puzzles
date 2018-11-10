class Solution:

    def __init__(self):
        self.mem_table = dict()

    def rob_cal(self, nums, index):
        if index in self.mem_table.keys():
            return self.mem_table[index]

        if index < 0:
            return 0

        if index == 0:
            return nums[index]

        self.mem_table[index] = max(nums[index] + self.rob_cal(nums, index - 2), self.rob_cal(nums, index - 1))

        return self.mem_table[index]

    def rob(self, nums):
        return self.rob_cal(nums, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()

    print(sol.rob([2, 1]))
