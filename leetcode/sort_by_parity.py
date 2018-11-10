class Solution:
    def sortArrayByParity(self, A):
        even_nums = list()
        odd_nums = list()

        for val in A:
            if val % 2 == 0:
                even_nums.append(val)
            else:
                odd_nums.append(val)

        return even_nums + odd_nums

