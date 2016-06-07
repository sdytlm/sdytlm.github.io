 class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a == None:
            return b
        if b== None:
            return a 
        
        ret = ""
        add = 0
        i = len(a)-1
        j = len(b)-1

        while i >= 0 and j >= 0:
            l = int(a[i])
            r = int(b[j])
            ret = str((l+r+add)%2)+ret
            add = (l+r+add)/2
            i -=1
            j -=1
        
        while i >= 0:
            l = int(a[i])
            ret = str((l+add)%2) + ret
            add = (l+add)/2
            i -= 1
        while j >= 0:
            r = int(b[j])
            ret = str((r+add)%2) + ret
            add = (r+add)/2
            j -= 1
        
        # don't forget add
        if add ==0:
            return ret
        else:
            return "1"+ret      
