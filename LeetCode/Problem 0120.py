from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(-2, -(len(triangle)) - 1, -1):
            for j in range(len(triangle[i])):
                pivot = triangle[i][j]
                l, r = triangle[i+1][j], triangle[i+1][j+1]
                triangle[i][j] = pivot + min(l, r)

        return triangle[0][0]
