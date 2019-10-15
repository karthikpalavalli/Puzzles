from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        idx = 0
        prices_len = len(prices)

        max_profit = list()

        while idx < prices_len - 1:
            while idx < prices_len - 1 and prices[idx] >= prices[idx + 1]:
                idx += 1

            valley = prices[idx]

            while idx < prices_len - 1 and prices[idx] <= prices[idx+1]:
                idx += 1

            peak = prices[idx]

            max_profit.append(peak - valley)

        return sum(max_profit)


if __name__ == "__main__":
    pass
