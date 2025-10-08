class Spreadsheet:

    sheet = []
    col_key = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
               'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

    def __init__(self, rows: int):
        self.sheet = []
        for i in range(rows):
            self.sheet.append([0] * 26)

    def setCell(self, cell: str, value: int) -> None:
        row = int(cell[1:]) - 1
        col = self.col_key[cell[0]]
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        sign_index = formula.find('+')
        values = [formula[1:sign_index], formula[sign_index + 1:]]
        new_values = []
        for i in range(len(values)):
            if values[i][0] in self.col_key.keys():
                row = int(values[i][1:]) - 1
                col = self.col_key[values[i][0]]
                new_values.append(self.sheet[row][col])
            else:
                new_values.append(int(values[i]))
        return new_values[0] + new_values[1]

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
