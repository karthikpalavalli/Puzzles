class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        concatenated_arr = list()
        nums1_it = 0
        nums2_it = 0
        nums1_len = len(nums1)
        nums2_len = len(nums2)

        for it in range(nums1_len + nums2_len):
            if nums1_it < nums1_len and nums2_it == nums2_len:
                concatenated_arr.append(nums1[nums1_it])
                nums1_it += 1

            elif nums1_it < nums1_len and nums1[nums1_it] <= nums2[nums2_it]:
                concatenated_arr.append(nums1[nums1_it])
                nums1_it += 1

            elif nums2_it < nums2_len and nums1_it == nums1_len:
                concatenated_arr.append(nums2[nums2_it])
                nums2_it += 1

            elif nums2_it < nums2_len and nums1[nums1_it] >= nums2[nums2_it]:
                concatenated_arr.append(nums2[nums2_it])
                nums2_it += 1

        len_concatenated_arr = len(concatenated_arr)

        if len_concatenated_arr % 2 == 0:
            mid_right = int(len_concatenated_arr/2.0)
            mid_left = mid_right - 1
            return (concatenated_arr[mid_left] + concatenated_arr[mid_right]) / 2.0

        else:
            mid = int(len_concatenated_arr/2.0)

            return concatenated_arr[mid]


sol = Solution()
nums1 = []
nums2 = [2,3]
sol.findMedianSortedArrays(nums1, nums2)