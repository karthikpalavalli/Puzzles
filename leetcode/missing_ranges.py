from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            return [self.generate_range_string(lower, upper)]

        missing_ranges = list()

        if nums[0] != lower:
            missing_ranges.append(str(lower) + "->" + str(nums[0] - 1))

        for idx in range(len(nums) - 1):
            potential_upper = nums[idx + 1] - 1
            potential_lower = nums[idx] + 1

            if potential_lower == potential_upper:
                missing_ranges.append(str(potential_lower))

            elif potential_upper > potential_lower:
                missing_ranges.append(str(potential_lower) + "->" + str(potential_upper))

        if nums[-1] != upper:
            missing_ranges.append(str(nums[-1] + 1) + "->" + str(upper))

        return missing_ranges

    def generate_range_string(self, lower, upper):
        if lower == upper:
            return str(lower)

        return str(lower) + "->" + str(upper)


if __name__ == "__main__":
    test_nums = [0, 1, 3, 50, 75]
    test_lower = 0
    test_upper = 99
    sol = Solution()

    print(sol.findMissingRanges(test_nums, test_lower, test_upper))
