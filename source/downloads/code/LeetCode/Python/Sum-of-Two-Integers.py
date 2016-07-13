class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ret = 0
        carry = 0
        for i in range(32):
            lower_a = a&1
            lower_b = b&1
            ret |=(lower_a ^ lower_b ^ carry) << i
            # carry,lower_a,lower_b: if two of them are '1', you need carry
            carry = (lower_a & lower_b) | (lower_a & carry) | (lower_b & carry)
            a = a>>1
            b = b>>1

            if a == 0 and b == 0 and carry==0:
                break
        return ret

if __name__ == "__main__":
    sol =Solution()
    print sol.getSum(2,3)
