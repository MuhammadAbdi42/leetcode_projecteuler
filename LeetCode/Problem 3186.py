from typing import List
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        damage = sorted(freq)
        n = len(damage)

        dp = [0] * n
        dp[0] = damage[0] * freq[damage[0]]
        for i in range(1,n):
            temp = damage[i] * freq[damage[i]]
            l, r, ans = 0, i - 1, -1
            while l <= r:
                mid = (l + r) // 2
                if damage[mid] <= damage[i] - 3:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            if ans >= 0:
                temp += dp[ans]
            dp[i] = max(dp[i-1], temp)
        
        return dp[-1]
