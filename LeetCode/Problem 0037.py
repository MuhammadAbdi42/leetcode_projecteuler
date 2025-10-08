from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board

        self.empty_cells = []
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] == '.':
                    self.empty_cells.append((i, j))
                else:
                    self.rows[i].add(board[i][j])
                    self.cols[j].add(board[i][j])
                    self.boxes[(i // 3) * 3 + j // 3].add(board[i][j])

        self.backtrack(0)

    def valid_options(self, point: tuple) -> set[str]:
        box = (point[0] // 3) * 3 + point[1] // 3
        return {str(x) for x in range(1, 10)} - self.rows[point[0]] - self.cols[point[1]] - self.boxes[box]

    def backtrack(self, index) -> bool:
        if index == len(self.empty_cells):
            return True

        cell = self.empty_cells[index]
        options = self.valid_options(cell)

        if not options:
            return False

        for option in options:
            self.board[cell[0]][cell[1]] = option
            self.rows[cell[0]].add(option)
            self.cols[cell[1]].add(option)
            self.boxes[(cell[0] // 3) * 3 + cell[1] // 3].add(option)

            if self.backtrack(index + 1):
                return True

            self.board[cell[0]][cell[1]] = '.'
            self.rows[cell[0]].remove(option)
            self.cols[cell[1]].remove(option)
            self.boxes[(cell[0] // 3) * 3 + cell[1] // 3].remove(option)

        return False
