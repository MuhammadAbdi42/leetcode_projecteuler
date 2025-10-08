from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hor_axis = (len(matrix) - 1) / 2
        center = (len(matrix) - 1) / 2

        i = 0
        while i < hor_axis:
            for j in range(i, len(matrix) - 1 - i):
                nw = (i, j)
                ne = (int(center - (center - j)), int(center + (center - i)))
                se = (int(center + (center - i)), int(center + (center - j)))
                sw = (int(center + (center - j)), int(center - (center - i)))

                nw_old = matrix[nw[0]][nw[1]]
                ne_old = matrix[ne[0]][ne[1]]
                se_old = matrix[se[0]][se[1]]
                sw_old = matrix[sw[0]][sw[1]]

                # NE = NW
                matrix[ne[0]][ne[1]] = nw_old

                # SE = NE
                matrix[se[0]][se[1]] = ne_old

                # SW = SE
                matrix[sw[0]][sw[1]] = se_old

                # NW = SW
                matrix[nw[0]][nw[1]] = sw_old

            i += 1
        print(matrix)
