from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        K = list(str(K))

        ptr1 = len(A) - 1
        ptr2 = len(K) - 1
        carry_forward = 0
        result = list()

        while ptr1 > -1 or ptr2 > -1:
            val1 = val2 = 0

            if ptr1 >= 0:
                val1 = A[ptr1]

            if ptr2 >= 0:
                val2 = int(K[ptr2])

            current_sum = carry_forward + val1 + val2

            if current_sum > 9:
                carry_forward = current_sum // 10
                current_sum = current_sum % 10

            else:
                carry_forward = 0

            result = [current_sum] + result
            ptr1 -= 1
            ptr2 -= 1

        if carry_forward:
            result = [carry_forward] + result

        return result


if __name__ == "__main__":
    sol = Solution()
    A = [1,2,0,0]
    K = 34
    print(sol.addToArrayForm(A, K))
