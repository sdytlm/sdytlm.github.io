class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = ""
        
        stack = []
        stack.append(["",0])
        for ch in s:
            #123456789
            if ch.isdigit():
                num += ch
            elif ch == '[':
                # 插入当前的num
                stack.append(["",int(num)])
                num = ""
            elif ch == ']':
                sub = stack[-1][0]*stack[-1][1]
                stack.pop()
                stack[-1][0] += sub
            else:
                # characters
                stack[-1][0] += ch
        return stack[0][0]
