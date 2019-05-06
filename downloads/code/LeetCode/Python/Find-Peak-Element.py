class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)/2
            if mid-1 < 0 and mid+1 < len(nums):
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    start = mid+1
            if mid+1 >= len(nums) and mid-1>=0:
                if nums[mid] > nums[mid-1]:
                    return mid
                else: 
                    end = mid-1

            if mid-1 >=0 and mid+1<len(nums):
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] < nums[mid-1]:
                    end = mid-1
                else: 
                    #nums[mid] < nums[mid+1]:
                    start = mid+1
        return start

if __name__ == "__main__":
    sol = Solution()
    sol.findPeakElement([3,2,1])
