class Solution:
    def isValid(self, s: str) -> bool:
        opening_closing = ['[]', '{}', '()', '']

        while s:
            old_s = s
            for item in opening_closing:
                s = s.replace(item, '')
            if old_s == s and s != '':
                return False

        return True
