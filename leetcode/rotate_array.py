from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        print(hex(id(nums)))

        # nums = nums[-k:] + nums[:len(nums) - k]
        nums.pop(2)

        print("Nums inside the function: ", nums)

        print(hex(id(nums)))

        # temp = nums[-k:]

        # for idx in range(len(nums) - 1, k - 1, -1):
        #     nums[idx] = nums[idx - k]
        #
        # for idx in range(0, k):
        #     nums[idx] = temp[idx]


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sol = Solution()
    sol.rotate(test_nums, 3)
    print("Nums at main: ", test_nums)


