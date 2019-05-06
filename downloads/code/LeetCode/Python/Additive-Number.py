class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
	n = len(num)
        for i,j in itertools.combinations(range(1,n),2):
            # 得到第一个数和第二个数
            a, b = num[:i], num[i:j]
            # a = "01" 以0开始
            if a != str(int(a)) or b != str(int(b)):
                continue
            while j < n:
                # c: 第三个数应该是多少
                c = str(int(a) + int(b))
                
                # 第三个数实际并不是c
                if not num.startswith(c,j):
                    break
                j += len(c)
                a,b = b,c
                if j == n:
                    return True
        return False
