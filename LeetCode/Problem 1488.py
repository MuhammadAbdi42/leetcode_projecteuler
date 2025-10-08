from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lake_rains = {}
        dry_days = []

        output = []
        for i in range(len(rains)):
            if rains[i] == 0:
                output.append(1)
                dry_days.append(i)
            else:
                output.append(-1)
                if rains[i] in lake_rains:
                    lake_rains[rains[i]].append(i)
                else:
                    lake_rains[rains[i]] = [i]

        for i in range(len(rains)):
            if rains[i] != 0:
                day_to_dry = lake_rains[rains[i]].index(i)
                if day_to_dry == 0:
                    continue
                else:
                    dried = False
                    for dry_day in dry_days:
                        if (dry_day > lake_rains[rains[i]][day_to_dry - 1] and
                                dry_day < lake_rains[rains[i]][day_to_dry]):
                            dried = True
                            output[dry_day] = rains[i]
                            dry_days.remove(dry_day)
                            break

                    if not dried:
                        return []

        return output
