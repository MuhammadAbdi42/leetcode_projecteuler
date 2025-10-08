from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        return self.func(candidates, target)

    def func(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        else:
            output = []
            for ind, candid in enumerate(candidates):
                if candid == target:
                    output.append([candid])
                elif candid > target:
                    break
                else:
                    rec = self.func(candidates[ind:], target - candid)
                    for i in range(len(rec)):
                        output.append([candid] + rec[i])
            return output
