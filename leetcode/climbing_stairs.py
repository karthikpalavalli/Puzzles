class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return n

        mem_table = list()
        mem_table.append(0)
        mem_table.append(1)
        mem_table.append(2)

        for idx in range(3, n + 1):
            mem_table.append(mem_table[idx - 1] + mem_table[idx - 2])

        return mem_table[n]