class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        duplicate_elements = list()
        final_element = len(list) + 1

        for num in nums:
            index = (num % final_element) - 1

            if nums[index] / final_element > 1.0:
                duplicate_elements.append(num)

            else:
                nums[index] += final_element

        return duplicate_elements