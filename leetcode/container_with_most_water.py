class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0

        l_iter = 0
        r_iter = len(height) - 1

        while l_iter < r_iter:
            max_water = max(max_water, min(height[l_iter], height[r_iter]) * (r_iter - l_iter))

            if height[l_iter] < height[r_iter]:
                l_iter += 1

            else:
                r_iter -= 1

        return max_water
