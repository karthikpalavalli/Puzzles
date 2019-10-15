from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = sys.maxsize
        max_profit = 0

        for val in prices:
            if val < min_value:
                min_value = val
            elif val - min_value > max_profit:
                max_profit = val - min_value

        return max_profit

