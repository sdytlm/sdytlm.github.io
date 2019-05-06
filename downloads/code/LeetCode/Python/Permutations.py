class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if not nums:
            return ret
        self.recP(nums,ret,[])
        return ret
    def recP(self,nums,ret,tmp):
        if len(nums) == 0:
            ret.append(tmp[:])
            return
        for i,j in enumerate(nums):
            tmp.append(j)
            nums.pop(i)
            self.recP(nums,ret,tmp)
            tmp.pop()
            nums.insert(i,j)

        
