class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        ret = ""
        if path == None or len(path) == 0:
            return 
        paths = path.split('/')
        stack = []
        for i in paths:
            if i == "..":
                if len(stack) != 0:
                    stack.pop()
            elif i == "." or i =="":
                continue
            else:
                stack.append(i)
        ret = '/'+'/'.join(stack)
        return ret
    
