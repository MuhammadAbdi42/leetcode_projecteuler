from typing import List


class Solution:
    pre_ns = [[], ['()']]

    def generateParenthesis(self, n: int) -> List[str]:
        last_n = len(self.pre_ns) - 1

        if n <= last_n:
            return self.pre_ns[n]

        elif n == last_n + 1:
            output = []
            l, r = 1, last_n
            while l <= r:
                for a in self.pre_ns[l]:
                    for b in self.pre_ns[r]:
                        new_para_1 = a + b
                        new_para_2 = b + a
                        if new_para_1 not in output:
                            output.append(new_para_1)
                        if new_para_2 not in output:
                            output.append(new_para_2)
                l += 1
                r -= 1

            for para in self.pre_ns[last_n]:
                new_para_1 = '(' + para + ')'
                if new_para_1 not in output:
                    output.append(new_para_1)

            self.pre_ns.append(output)
            return self.pre_ns[n]

        else:
            for i in range(last_n + 1, n + 1):
                self.generateParenthesis(i)
            return self.pre_ns[n]
