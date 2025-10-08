from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def canReachEnd(time: int) -> bool:
            if grid[0][0] > time:
                return False

            visited = set([(0, 0)])
            stack = [(0, 0)]

            while stack:
                i, j = stack.pop()
                if (i, j) == (n - 1, n - 1):
                    return True

                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if (0 <= ni < n and 0 <= nj < n and
                        (ni, nj) not in visited and
                            grid[ni][nj] <= time):
                        visited.add((ni, nj))
                        stack.append((ni, nj))
            return False

        # Binary search the minimum time
        lo, hi = max(grid[0][0], grid[-1][-1]), n**2 - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if canReachEnd(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
