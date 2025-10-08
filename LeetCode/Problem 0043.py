class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_to_char = {
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'
        }
        char_to_digit = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }

        str_nums, nums = [num1, num2], [0, 0]
        for i in range(len(str_nums)):
            for j in range(len(str_nums[i])):
                nums[i] *= 10
                nums[i] += char_to_digit[str_nums[i][j]]

        multi = nums[0] * nums[1]
        output = ''

        if multi == 0:
            return '0'

        while multi > 0:
            digit = multi % 10
            multi = multi // 10
            output = digit_to_char[digit] + output

        return output
