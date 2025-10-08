from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        output = []
        for spell in spells:
            l, r = 0, len(potions) - 1

            if potions[0] * spell >= success:
                output.append(len(potions))
            elif potions[-1] * spell < success:
                output.append(0)
            else:
                l, r = 0, len(potions) - 1

                while l < r:
                    if l + 1 == r:
                        output.append(len(potions) - r)
                        break

                    mid = (l + r) // 2
                    if potions[mid] * spell >= success:
                        r = mid
                    else:
                        l = mid

        return output
