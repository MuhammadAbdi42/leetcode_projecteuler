class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            s = self.countAndSay(n - 1)
            output = ''
            while s:
                sub_s = s[0]
                i = 1
                while i < len(s) and s[i] == sub_s[0]:
                    sub_s += s[i]
                    i += 1
                s = s[i:]
                output += str(len(sub_s)) + sub_s[0]
            return output
