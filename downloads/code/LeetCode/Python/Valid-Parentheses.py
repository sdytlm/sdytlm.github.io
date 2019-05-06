class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top == '(' and c != ')':
                    return False
                if top == '{' and c != '}':
                    return False
                if top == '[' and c != ']':
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


