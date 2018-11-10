from copy import deepcopy

class Solution:

    def isValidSudoku(self, board):
        row_dict = {i: list() for i in range(9)}
        col_dict = deepcopy(row_dict)
        box_dict = deepcopy(row_dict)

        for i in range(9):

            for j in range(9):

                if board[i][j] != ".":
                    board_id = (i // 3) * 3 + j // 3

                    if self.check_in_list(board[i][j], row_dict[i]) and \
                            self.check_in_list(board[i][j], col_dict[j]) and \
                            self.check_in_list(board[i][j], box_dict[board_id]):

                        row_dict[i].append(board[i][j])
                        col_dict[j].append(board[i][j])
                        box_dict[board_id].append(board[i][j])

                    else:
                        return False

        return True

    @classmethod
    def check_in_list(cls, element, element_list):
        if element in element_list:
            return False

        return True


if __name__ == "__main__":
    sol = Solution()

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]

    print(sol.isValidSudoku(board))
