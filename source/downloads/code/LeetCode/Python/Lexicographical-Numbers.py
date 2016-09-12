
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        stack = [1]
        ret = []
        while stack:
            top = stack.pop()
            ret.append(top)
            #各位数字小于9
            # 一定要先插个位数字小于９的，再插top*10
            if top < n and top % 10 < 9:
                stack.append(top+1)
            if top * 10 <= n:
                stack.append(top*10)
        return ret
