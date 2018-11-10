class Solution:
    def checkPerfectNumber(self, num):

        sum_positive_divisors = 0

        for it in range(1, int(num ** 0.5) + 1):
            if num % it == 0:
                sum_positive_divisors += it

                if it * it != num:
                    sum_positive_divisors += num / it

        if sum_positive_divisors == num:
            return True

        return False
