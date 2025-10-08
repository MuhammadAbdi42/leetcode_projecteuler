import math


class Solution:
    def climbStairs(self, n: int) -> int:
        output = 0
        one_step = n
        two_step = 0
        while one_step >= 0:
            output += math.factorial(one_step + two_step) / \
                (math.factorial(one_step) * math.factorial(two_step))

            one_step -= 2
            two_step += 1

        return int(output)
