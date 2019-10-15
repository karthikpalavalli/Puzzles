from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write_pointer = n + m - 1
        n -= 1
        m -= 1

        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[write_pointer] = nums1[m]
                m -= 1

            else:
                nums1[write_pointer] = nums2[n]
                n -= 1

            write_pointer -= 1

        nums1[:n+1] = nums2[:n+1]


if __name__ == "__main__":
    sol = Solution()

    nums1 = [8, 9, 10, 0, 0, 0]
    nums2 = [4, 5, 6]

    sol.merge(nums1, 3, nums2, len(nums2))