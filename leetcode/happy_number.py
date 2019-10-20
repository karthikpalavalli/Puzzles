class Solution:
    def compute_squares(self, num) -> int:
        square_sum = 0

        while num:
            digit = num % 10
            square_sum += digit ** 2
            num //= 10

        return square_sum

    def isHappy(self, n: int) -> bool:
        visited_numbers = list()
        visited_numbers.append(n)

        while True:
            n = self.compute_squares(n)

            if n in visited_numbers:
                return False

            elif n == 1:
                return True

            visited_numbers.append(n)


if __name__ == "__main__":
    test_n = 19

    sol = Solution()
    print(sol.isHappy(test_n))