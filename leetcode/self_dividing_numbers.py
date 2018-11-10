class Solution:
    def selfDividingNumbers(self, left, right):
        numbers = [num for num in range(left, right + 1)]

        self_dividing_numbers = list()

        for num in numbers:
            str_num = str(num)

            if '0' in str_num:
                continue

            self_div_flag = True

            for digit in str_num:
                if num % int(digit) != 0:
                    self_div_flag = False
                    break

            if self_div_flag:
                self_dividing_numbers.append(num)

        return self_dividing_numbers
