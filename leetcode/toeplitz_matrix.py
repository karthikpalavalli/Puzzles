from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        is_toeplitz = True

        row_len = len(matrix)
        col_len = len(matrix[0])

        for idx in range(0, row_len):
            row_iter = idx
            col_iter = 0

            val = matrix[row_iter][col_iter]

            while row_iter < row_len and col_iter < col_len:
                if matrix[row_iter][col_iter] != val:
                    is_toeplitz = False
                    break

                row_iter += 1
                col_iter += 1

        for idx in range(0, col_len):
            col_iter = idx
            row_iter = 0

            val = matrix[row_iter][col_iter]

            while row_iter < row_len and col_iter < col_len:
                if matrix[row_iter][col_iter] != val:
                    is_toeplitz = False
                    break

                row_iter += 1
                col_iter += 1

        return is_toeplitz


if __name__ == "__main__":
    test_matrix = [[11,74,0,93],[40,11,74,7]]

    sol = Solution()
    print(sol.isToeplitzMatrix(test_matrix))