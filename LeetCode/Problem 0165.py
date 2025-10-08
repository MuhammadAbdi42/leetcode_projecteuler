class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1, ver2 = version1.split('.'), version2.split('.')
        ver1, ver2 = list(map(lambda x: int(x), ver1)), list(
            map(lambda x: int(x), ver2))

        i = len(ver1) - 1
        while ver1[i] == 0 and len(ver1) > 1:
            ver1.pop()
            i -= 1

        i = len(ver2) - 1
        while ver2[i] == 0 and len(ver2) > 1:
            ver2.pop()
            i -= 1

        i = 0
        while True:
            if i == len(ver1) and i < len(ver2):
                return -1
            elif i < len(ver1) and i == len(ver2):
                return 1
            elif i == len(ver1) and i == len(ver2):
                return 0
            else:
                if ver1[i] > ver2[i]:
                    return 1
                elif ver1[i] < ver2[i]:
                    return -1
                else:
                    i += 1
