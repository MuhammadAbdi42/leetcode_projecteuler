class Solution:
    def longestValidParentheses(self, s: str) -> int:
        i = 0
        while True:
            check_str = '(' + ('-' * (i*2)) + ')'
            if len(check_str) > len(s):
                break
            else:
                s = s.replace(check_str, '-' * ((i+1)*2))
                i += 1

        output = 0
        i = 0
        while True:
            check_str = ('-' * (i*2))
            if len(check_str) > len(s):
                break
            else:
                if check_str in s:
                    output = i * 2
                else:

                    break
                i += 1

        return output
