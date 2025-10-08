class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank, empty = 0, 0
        while True:
            drank += numBottles
            empty += numBottles
            numBottles = empty // numExchange
            empty = empty % numExchange

            if empty < numExchange and numBottles == 0:
                break

        return drank
