from typing import List
import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        for i in range(n):
            board.append([])
        for i in range(n):
            for j in range(n):
                board[i].append(' ')

        boards = self.solve(board)

        output = []
        for _board in boards:
            new_board = []
            for _row in _board:
                new_row = ''
                for _cell in _row:
                    new_row += _cell
                new_board.append(new_row)
            output.append(new_board)

        return output

    def solve(self, board: List[List[str]]) -> List[List[List[str]]]:
        # Checking for end states (Enough queens for True/No more safe spots for False)
        queen_count = 0
        safe_spots = []

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'Q':
                    queen_count += 1
                elif board[i][j] == ' ':
                    safe_spots.append((i, j))

        if queen_count == len(board):
            return [board]
        elif safe_spots == []:
            return []
        else:
            # Iterating on safespots in the first safe row (next rows don't need to be seen)
            first_safe_row = safe_spots[0][0]
            output = []
            for safe_spot in safe_spots:
                if safe_spot[0] > first_safe_row:
                    break

                output += self.solve(self.queen_placement(copy.deepcopy(board),
                                     safe_spot[0], safe_spot[1]))

            return output

    def queen_placement(self, board: List[List[str]], row: int, column: int) -> List[List[str]]:
        board[row][column] = 'Q'

        # Row and Columns
        for i in range(len(board)):
            if i != row:
                board[i][column] = '.'
            if i != column:
                board[row][i] = '.'

        # Four diagonals
            # NE
        r, c = row - 1, column - 1
        while 0 <= r < len(board) and 0 <= c < len(board):
            board[r][c] = '.'
            r -= 1
            c -= 1

            # NW
        r, c = row - 1, column + 1
        while 0 <= r < len(board) and 0 <= c < len(board):
            board[r][c] = '.'
            r -= 1
            c += 1

            # SE
        r, c = row + 1, column - 1
        while 0 <= r < len(board) and 0 <= c < len(board):
            board[r][c] = '.'
            r += 1
            c -= 1

            # SW
        r, c = row + 1, column + 1
        while 0 <= r < len(board) and 0 <= c < len(board):
            board[r][c] = '.'
            r += 1
            c += 1

        return board
