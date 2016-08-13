class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {x: False for x in nums}

        for i in hash_map:
            if hash_map[i] == False:
                # find up
                up = i
                while up in hash_map:
                    hash_map[up] = True
                    up +=1
                # find down
                down = i-1
                while down in hash_map:
                    hash_map[down] = True
                    down -= 1

                if (up-down-1>max):
                    max = up-down-1
        return max
