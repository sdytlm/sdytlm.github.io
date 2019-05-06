class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrimes = [True]*max(n,2)
        i = 2
        isPrimes[0] = False
        isPrimes[1] = False
        while i*i < n:
            if isPrimes[i]:
                # 把isPrimes[i的倍数]设置成false
                # 从i*i开始
                j = i*i
                while j < n:
                    isPrimes[j] = False
                    j += i
        
            i += 1
        
        # 统计所有True的数量
       
        return sum(isPrimes)
