class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        set_bits = 0

        while n:
            n = n & (n - 1)
            set_bits += 1

        if set_bits == 1:
            return True

        return False
