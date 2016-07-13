class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        ans = 1
        mod = 1337
        for bi in b[::-1]:
            ans = ans*a**bi%mod
            a = a ** 10 % mod
        return ans
