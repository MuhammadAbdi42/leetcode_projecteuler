class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = ' ' + s, ' ' + p

        dp = [[True] * len(p) for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(p)):
                if i == 0 and j == 0:
                    continue
                
                if s[i] == p[j] or (p[j] == '?' and s[i] != ' '):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    if i > 0:
                        dp[i][j] = dp[i-1][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = False

        return dp[-1][-1]
