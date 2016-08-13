class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        
        s1 = version1.split('.')
        s2 = version2.split('.')

        i = 0
        j = 0
        
        while i<len(s1) and j < len(s2):
            if int(s1[i]) < int(s2[j]):
                return -1
            if int(s1[i]) > int(s2[j]):
                return 1
            i += 1
            j += 1
        
        while i < len(s1):
            if int(s1[i]) != 0:
                return 1
            i += 1 

        while j < len(s2):
            if int(s2[j]) != 0:
                return -1
            j += 1
        return 0
