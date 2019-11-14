from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1

        for idx in range(len(digits) - 1, -1, -1):
            digit_at_idx = digits[idx]

            current_sum, remainder = (digit_at_idx + remainder) % 10, (digit_at_idx + remainder) // 10

            digits[idx] = current_sum

        return digits
