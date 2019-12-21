class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_product = 1
        n_sum = 0

        while n:
            digit = n % 10

            n_product *= digit
            n_sum += digit

            n = n // 10

        return n_product - n_sum
