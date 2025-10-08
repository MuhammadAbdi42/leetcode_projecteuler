class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        is_negative = False
        if (numerator < 0 and denominator > 0) or (numerator >= 0 and denominator < 0):
            is_negative = True
        numerator, denominator = abs(numerator), abs(denominator)
        whole_part, fraction_part = 0, ''
        remainders = {}

        if is_negative:
            negative_str = '-'
        else:
            negative_str = ''

        whole_part = (numerator // denominator)
        numerator = (numerator % denominator) * 10

        reaccuring, ind = False, 0
        while numerator != 0:
            remainder = numerator % denominator

            if remainder in remainders and remainders[remainder][1] == numerator // denominator:
                reaccuring = True
                start, end = remainders[remainder][0], ind - 1
                break
            else:
                remainders[remainder] = (ind, numerator // denominator)
                fraction_part += str(numerator // denominator)
                numerator = remainder * 10
                ind += 1

        if not fraction_part:
            return f'{negative_str}{whole_part}'
        else:
            if reaccuring:
                return f'{negative_str}{whole_part}.{fraction_part[:start]}({fraction_part[start: end+1]})'
            else:
                return f'{negative_str}{whole_part}.{fraction_part}'
