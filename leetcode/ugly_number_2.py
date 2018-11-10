class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        list_of_uglies = list()

        curr_iter = 0

        curr_val = 1
        list_of_uglies.append(curr_val)

        while len(list_of_uglies) != n:

            if curr_iter % 3 == 0:
                curr_val *= 2
            if curr_iter % 3 == 1:
                curr_val *= 3
            if curr_iter % 3 == 2:
                curr_val *= 5

            list_of_uglies.append(curr_val)
            curr_iter += 1

        return list_of_uglies[n-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.nthUglyNumber(10))