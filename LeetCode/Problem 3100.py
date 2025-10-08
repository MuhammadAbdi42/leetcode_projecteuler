class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank, empty = numBottles, numBottles
        while empty >= numExchange:
            drank += 1
            empty -= numExchange - 1
            numExchange += 1

        return drank
