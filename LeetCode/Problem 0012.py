class Solution:
    def intToRoman(self, num: int) -> str:
        num_str = str(num / 10000).split('.')[1]
        while len(num_str) < 4:
            num_str += '0'
        digit_1000 = int(num_str[0])
        digit_100 = int(num_str[1])
        digit_10 = int(num_str[2])
        digit_1 = int(num_str[3])

        output = ''

        output += 'M' * digit_1000

        if digit_100 == 4:
            output += 'CD'
        elif digit_100 == 9:
            output += 'CM'
        else:
            if digit_100 >= 5:
                output += 'D' + ('C' * (digit_100 - 5))
            elif digit_100 > 0:
                output += 'C' * digit_100

        if digit_10 == 4:
            output += 'XL'
        elif digit_10 == 9:
            output += 'XC'
        else:
            if digit_10 >= 5:
                output += 'L' + ('X' * (digit_10 - 5))
            elif digit_10 > 0:
                output += 'X' * digit_10

        if digit_1 == 4:
            output += 'IV'
        elif digit_1 == 9:
            output += 'IX'
        else:
            if digit_1 >= 5:
                output += 'V' + ('I' * (digit_1 - 5))
            elif digit_1 > 0:
                output += 'I' * digit_1

        return output
