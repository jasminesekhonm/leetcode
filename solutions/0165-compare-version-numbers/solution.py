class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        version1 = [int(v) for v in version1]
        version2 = [int(v) for v in version2]

        print(version1)
        print(version2)
        for i in range(min(len(version1), len(version2))):
            if version1[i] > version2[i]:
                return 1
            elif version1[i] < version2[i]:
                return -1
        
        version1 = [v for v in version1 if v != 0]
        version2 = [v for v in version2 if v != 0]

        if len(version1) == len(version2):
            return 0 
        elif len(version1) > len(version2):
            return 1 
        return -1
