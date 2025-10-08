class Solution:
    def myAtoi(self, s: str) -> int:
        int_limits = (- (2 ** 31), (2 ** 31) - 1)
        digits = '0123456789'

        s = s.strip()
        if s == '':
            return 0

        if s[0] == '+':
            negative = 1
            s = s[1:]
        elif s[0] == '-':
            negative = -1
            s = s[1:]
        elif s[0] not in digits:
            return 0
        else:
            negative = 1
        if s == '':
            return 0

        number = ''
        index = 0
        while s[index] in digits:
            number += s[index]
            index += 1
            if index > len(s) - 1:
                break

        if number == '':
            return 0

        number = int(number) * negative
        if number > int_limits[1]:
            return int_limits[1]
        elif number < int_limits[0]:
            return int_limits[0]
        else:
            return number
