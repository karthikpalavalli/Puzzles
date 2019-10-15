from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = list()

        result_arr.append(1)

        prod_left = 1

        for idx in range(1, len(nums)):
            prod_left *= nums[idx - 1]
            result_arr.append(prod_left)

        prod_right = 1

        for idx in range(len(nums) - 1, -1, -1):
            result_arr[idx] *= prod_right
            prod_right *= nums[idx]

        return result_arr


if __name__ == "__main__":
    sol = Solution()
    vals = [1, 4, 9, 11]
    print(sol.productExceptSelf(vals))
