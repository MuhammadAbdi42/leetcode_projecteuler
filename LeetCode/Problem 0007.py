class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        int_limits = (- (2 ** 31), (2 ** 31) - 1)

        if is_negative:
            reversed_str = (str(x)[1:])[::-1]
        else:
            reversed_str = str(x)[::-1]

        if len(reversed_str) < len(str(int_limits[1])):
            if is_negative:
                return - int(reversed_str)
            else:
                return int(reversed_str)
        else:
            if is_negative:
                limit_str = str(int_limits[0])[1:]
                for ind, digit in enumerate(reversed_str):
                    if int(digit) > int(limit_str[ind]):
                        return 0
                    elif int(digit) == int(limit_str[ind]):
                        continue
                    else:
                        return - int(reversed_str)
                return - int(reversed_str)
            else:
                limit_str = str(int_limits[1])
                for ind, digit in enumerate(reversed_str):
                    if int(digit) > int(limit_str[ind]):
                        return 0
                    elif int(digit) == int(limit_str[ind]):
                        continue
                    else:
                        return int(reversed_str)
                return int(reversed_str)
