class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ptr2 = 0

        carry_forward = 0

        result = ["0"] * len(num1)

        while ptr2 != len(num2):
            ptr1 = len(num1) - 1
            val2 = num2[ptr2]
            ptr_result = len(result) - 1

            print(result)

            while ptr1 >= 0:
                val1 = num1[ptr1]
                ptr1 -= 1

                current_sum = carry_forward + int(val1) * int(val2) + int(result[ptr_result])

                carry_forward, current_sum = divmod(current_sum, 10)

                result[ptr_result] = str(current_sum)

                ptr_result -= 1

            if carry_forward:
                if ptr_result:
                    result[ptr_result] = str(carry_forward + int(result[ptr_result]))
                else:
                    result = [str(carry_forward)] + result

            result.append("0")

            ptr2 += 1

        print(result[:-1])

        return "".join(result[:-1])


if __name__ == "__main__":
    sol = Solution()

    num1 = "99"
    num2 = "99"

    sol.multiply(num1, num2)
