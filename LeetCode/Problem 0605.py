from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valid = 0

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            valid += 1
        else:
            for i in range(len(flowerbed)):
                if flowerbed[i] == 0:
                    if i == 0:
                        if flowerbed[1] == 0:
                            valid += 1
                            flowerbed[i] = 1
                    elif i == len(flowerbed) - 1:
                        if flowerbed[len(flowerbed) - 2] == 0:
                            valid += 1
                            flowerbed[i] = 1
                    else:
                        if flowerbed[i - 1] == 0 and flowerbed[i+1] == 0:
                            valid += 1
                            flowerbed[i] = 1

        return valid >= n
