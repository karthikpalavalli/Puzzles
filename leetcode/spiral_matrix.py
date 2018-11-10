class Solution:

    def spiralOrder(self, matrix):

        if not matrix:
            return []

        spiral_matrix = list()
        row_len, col_len = len(matrix), len(matrix[0])

        row_iter = 0
        col_iter = 0

        while row_iter < row_len and col_iter < col_len:

            for i in range(col_iter, col_len):
                spiral_matrix.append(matrix[row_iter][i])

            row_iter += 1

            for i in range(row_iter, row_len):
                spiral_matrix.append(matrix[i][col_len - 1])

            col_len -= 1

            if row_iter < row_len:
                for i in range(col_len - 1, col_iter - 1, -1):
                    spiral_matrix.append(matrix[row_len - 1][i])

                row_len -= 1

            if col_iter < col_len:
                for i in range(row_len - 1, row_iter - 1, -1):
                    spiral_matrix.append(matrix[i][col_iter])

                col_iter += 1

        return spiral_matrix


if __name__ == "__main__":
    sol = Solution()

    matrix = [[]]

    sol.spiralOrder()
