class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_matrix = [''] * numRows

        if numRows == 1:
            section_count = 1
        else:
            section_count = numRows*2 - 2

        for ind, char in enumerate(s):
            if (ind % section_count < numRows):
                zigzag_matrix[ind % section_count] += char
            else:
                selected_row = (numRows - 1) - \
                    ((ind % section_count) - (numRows - 1))
                for ind_row, row in enumerate(zigzag_matrix):
                    if ind_row == selected_row:
                        zigzag_matrix[ind_row] += char

        output = ''
        for row in zigzag_matrix:
            output += row

        return output
