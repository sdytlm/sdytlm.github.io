class Solution(object):
   def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        #Generate the sequence
        k = k-1
        nums = [i for i in range(1,n+1)]
        factorial = 1
        # calculate (n-1)!
        for i in range(1,n):
            factorial *= i 
        ret = ""
        for i in range(n-1,-1,-1):
            ret += str(nums[k/factorial])
            nums.remove(nums[k/factorial])
            if i!=0:
                k = k%factorial
                factorial = factorial/i
        return ret

