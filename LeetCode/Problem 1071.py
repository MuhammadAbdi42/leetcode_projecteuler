class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        output = ''
        i = 1
        while i < len(str1) + 1 and i < len(str2) + 1:
            if str1[:i] != str2[:i]:
                break
            else:
                if self.is_divisor(str1, str1[:i]) and self.is_divisor(str2, str2[:i]):
                    output = str1[:i]
            i += 1

        return output

    def is_divisor(self, s: str, p: str) -> bool:
        if len(s) % len(p) == 0:
            if s == p * int(len(s) / len(p)):
                return True

        return False
