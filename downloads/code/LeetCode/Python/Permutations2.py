class Solution(object):
    def rec(self, ret, tmp, nums):
        if len(nums) == 0 and tmp not in ret:
            ret.append(tmp[:])
            return

        for i,j in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            del nums[i]
            tmp.append(j)
            self.rec(ret,tmp,nums)
            nums.insert(i,j)
            tmp.pop()
        return

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret =[]
        if len(nums) == 0:
            return ret
    
        self.rec(ret,[],sorted(nums))
        return ret

if __name__ == "__main__":
    sol = Solution()
    sol.permuteUnique([1,1,2]
