class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary_n = list()

        while n:
            if n % 2 == 0:
                binary_n.append(0)
            else:
                binary_n.append(1)

            n = int(n/2)

        binary_n = list(reversed(binary_n))

        has_alternating_bits = True

        for iter in range(len(binary_n) - 1):
            if binary_n[iter] ^ binary_n[iter + 1] != 1:
                has_alternating_bits = False
                break

        return has_alternating_bits


if __name__ == "__main__":
    sol = Solution()

    print(sol.hasAlternatingBits(3))