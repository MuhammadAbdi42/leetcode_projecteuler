from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    c = board[i][j]
                    board[i][j] = '.'
                    if not self.is_valid(board, i, j, c):
                        return False
                    board[i][j] = c

        return True

    def is_valid(self, board, row, col, option):
        for i in range(9):
            if board[row][i] == option or board[i][col] == option:
                return False

        # Checking the 3x3 grid
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == option:
                    return False

        return True
