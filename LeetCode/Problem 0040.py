from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        return self.func(candidates, target)

    def func(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []

        else:
            output = []
            last_processed = 0
            for ind, candid in enumerate(candidates):
                if candid == target:
                    if [candid] not in output:
                        output.append([candid])
                elif candid > target:
                    break
                else:
                    if last_processed == candid:
                        continue
                    else:
                        last_processed = candid
                    rec = self.func(candidates[ind+1:], target - candid)
                    for i in range(len(rec)):
                        if sorted([candid] + rec[i]) not in output:
                            output.append(sorted([candid] + rec[i]))
            return output
