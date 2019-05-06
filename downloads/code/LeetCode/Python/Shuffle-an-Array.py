class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.orig = nums[:]
        self.shuffled_nums = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.shuffled_nums = self.orig[:]
        return self.orig


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = len(self.shuffled_nums)
        for i in range(n):
            newindex = random.randint(0,i)
            self.shuffled_nums[i],self.shuffled_nums[newindex] = self.shuffled_nums[newindex],self.shuffled_nums[i]
	return self.shuffled_nums

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
