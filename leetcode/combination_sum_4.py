class Solution():
    def combinationSum4(self, nums, target):

        comb = [0] * (target + 1)

        comb[0] = 1

        for i in range(1, len(comb)):
            for j in range(len(nums)):
                if i - nums[j] >= 0:
                    comb[i] += comb[i - nums[j]]

        print("Comb:", comb)
        return comb[target]


if __name__ == "__main__":
    sol = Solution()

    target = 4
    day_hours = 4

    nums = [i for i in range(day_hours + 1)]
    print("Nums: ", nums)

    print(sol.combinationSum4(nums, target))