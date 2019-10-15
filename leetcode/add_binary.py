class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ptr1 = len(a) - 1
        ptr2 = len(b) - 1

        carry_forward = 0

        result = str()

        while ptr1 > -1 or ptr2 > -1:
            val1 = val2 = 0

            if ptr1 >= 0:
                val1 = a[ptr1]
                ptr1 -= 1

            if ptr2 >= 0:
                val2 = b[ptr2]
                ptr2 -= 1

            current_sum = carry_forward + int(val1) + int(val2)

            carry_forward, current_sum = divmod(current_sum, 2)

            result = str(current_sum) + result

        if carry_forward:
            result = str(carry_forward) + result

        return result


if __name__ == "__main__":
    sol = Solution()

    bin1 = '1010'
    bin2 = '1011'

    print(sol.addBinary(bin1, bin2))