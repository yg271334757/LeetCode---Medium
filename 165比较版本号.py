class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        v1 = [int(a) for a in v1]
        v2 = [int(a) for a in v2]
        if len(v1) > len(v2):
            for _ in range(len(v1) - len(v2)):
                v2.append(0)
        elif len(v2) > len(v1):
            for _ in range(len(v2) - len(v1)):
                v1.append(0)
        for j in range(len(v1)):
            if v1[j] > v2[j]:
                return 1
            elif v1[j] < v2[j]:
                return -1
        return 0
