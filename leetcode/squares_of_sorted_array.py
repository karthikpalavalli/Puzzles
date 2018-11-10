import sys


class Solution:

    def sortedSquares(self, A):

        pos_ptr = 0

        while A[pos_ptr] < 0:
            pos_ptr += 1

        if len(A) == 1:
            return [A[0] ** 2]

        neg_ptr = pos_ptr - 1

        squared_number = list()

        while len(squared_number) != len(A):

            # pos pointer
            if pos_ptr == len(A):
                pos_ptr_sq = sys.maxsize

            else:
                pos_ptr_sq = A[pos_ptr] ** 2

            # neg pointer
            if neg_ptr == -1:
                neg_ptr_sq = sys.maxsize

            else:
                neg_ptr_sq = A[neg_ptr] ** 2

            # comparison and update
            if pos_ptr_sq < neg_ptr_sq:
                squared_number.append(pos_ptr_sq)
                pos_ptr += 1

            else:
                squared_number.append(neg_ptr_sq)
                neg_ptr -= 1

        return squared_number


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedSquares([-4, -1, 0, 3, 10]))
