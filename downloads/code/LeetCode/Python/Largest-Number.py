class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return ""
        s = [str(x) for x in nums]
        sorted_s = sorted(s,cmp=self.compare)
        ret = "".join(sorted_s).lstrip('0')
        if ret != "":
            return ret
        else:
            return "0"


    def compare(self,a,b):
        return [1,-1][a+b>b+a]
    
        
