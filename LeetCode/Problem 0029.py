class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_LIMITS = (- (2 ** 31), (2 ** 31) - 1)

        negative = (dividend >= 0 and divisor < 0) or (
            dividend < 0 and divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        digits = str(dividend)
        output = 0

        pivot = 0
        digits = digits
        while pivot <= divisor and digits:
            pivot = pivot * 10 + int(digits[0])
            digits = digits[1:]

        while pivot >= divisor:
            pivot -= divisor
            output += 1

        while digits:
            pivot = pivot * 10 + int(digits[0])
            digits = digits[1:]

            output *= 10
            while pivot >= divisor:
                pivot -= divisor
                output += 1

        if negative:
            output = -output

        if output < INT_LIMITS[0]:
            return INT_LIMITS[0]
        elif output > INT_LIMITS[1]:
            return INT_LIMITS[1]
        else:
            return output
