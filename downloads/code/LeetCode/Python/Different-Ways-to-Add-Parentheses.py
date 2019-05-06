class Solution(object):
    def cal(self, a,b,op):
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        else:
            return a*b

    def dfs(self, nums, ops):
        if not ops:
            return [nums[0]]
        
        # find split the nums and merge
        ans = []
        for op in range(len(ops)):
            left = self.dfs(nums[:op+1],ops[:op])
            right = self.dfs(nums[op+1:],ops[op+1:])
            for a in left:
                for b in right:
                    ans.append(self.cal(a,b,ops[op]))

        return ans

    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        operator = "+-*"
        nums = []
        ops = []

        # split input
        s = re.split('(\D)', input)
        for i in s:
            if i in operator:
                ops.append(i)
            else:
                nums.append(int(i))

        return self.dfs(nums,ops)
