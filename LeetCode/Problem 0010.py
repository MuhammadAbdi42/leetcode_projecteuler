class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        is_match = True
        while True:
            if (p == '' and s != ''):
                is_match = False
                break
            elif (p != '' and s == ''):
                if (len(p) > 1):
                    if (p[1] == '*'):
                        return self.isMatch(s, p[2:])
                    else:
                        is_match = False
                        break
                else:
                    is_match = False
                    break
            elif (p == '' and s == ''):
                break

            # ./ .a/ .*
            if p[0] == '.':
                if (len(p) == 1):
                    s = s[1:]
                    p = p[1:]
                else:
                    if (p[1] == '*'):
                        for ind, char in enumerate(s):
                            if self.isMatch(s[ind:], p[2:]):
                                return True
                        if self.isMatch('', p[2:]):
                            return True
                        return False
                    else:
                        p = p[1:]
                        s = s[1:]

            # a/ a*/ ab
            elif p[0] != '.':
                if (len(p) == 1):
                    if (p[0] == s[0]):
                        p = p[1:]
                        s = s[1:]
                    else:
                        is_match = False
                        break
                else:
                    if p[1] != '*':
                        if (p[0] == s[0]):
                            p = p[1:]
                            s = s[1:]
                        else:
                            is_match = False
                            break
                    else:
                        index = -1
                        for char in s:
                            if char != p[0]:
                                break
                            else:
                                index += 1

                        if index == -1:
                            p = p[2:]
                        else:
                            for i in range(0, index+2):
                                if self.isMatch(s[i:], p[2:]):
                                    return True
                            return False

        return is_match
