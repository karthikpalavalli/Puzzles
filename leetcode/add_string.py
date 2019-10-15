class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ptr1 = len(num1) - 1
        ptr2 = len(num2) - 1
        carry_forward = 0
        result = str()

        while ptr1 > -1 or ptr2 > -1:
            val1 = val2 = 0

            if ptr1 >= 0:
                val1 = int(num1[ptr1])

            if ptr2 >= 0:
                val2 = int(num2[ptr2])

            current_sum = carry_forward + val1 + val2

            if current_sum > 9:
                carry_forward = current_sum // 10
                current_sum = current_sum % 10

            else:
                carry_forward = 0

            result = str(current_sum) + result
            ptr1 -= 1
            ptr2 -= 1

            print(ptr1, " ", ptr2)

        if carry_forward:
            result = str(carry_forward) + result

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.addStrings("9", "99"))
