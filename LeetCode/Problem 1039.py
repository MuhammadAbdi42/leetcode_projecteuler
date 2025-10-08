from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        dp = [[-1] * len(values) for _ in range(len(values))]

        def solve_dp(a, b) -> int:
            if dp[a][b] != -1:
                return dp[a][b]
            else:
                if b - a < 2:
                    dp[a][b] = 0
                else:
                    best = float('inf')
                    for i in range(a + 1, b):
                        option = (values[a]*values[b]
                                  * values[i] + solve_dp(a, i) + solve_dp(i, b))
                        best = min(best, option)
                    dp[a][b] = best

                return dp[a][b]

        return solve_dp(0, len(values) - 1)
