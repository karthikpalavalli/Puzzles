from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1], [1, 1]]

        if numRows == 0 or numRows == 1 or numRows == 2:
            return triangle[:numRows]

        while len(triangle) < numRows:
            current_row = [1]

            for idx in range(len(triangle[-1]) - 1):
                current_row.append(triangle[-1][idx] + triangle[-1][idx + 1])

            current_row.append(1)
            triangle.append(current_row)

        return triangle


if __name__ == "__main__":
    sol = Solution()
    sol.generate(4)
