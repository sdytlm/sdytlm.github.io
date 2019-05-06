class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size

# 2d array
    def backPack(self, m, A):
        # write your code here
        l = len(A)
        s = min(max(A),m)
        dp = [[0]*(s+1) for i in range(l+1)]
        for i in range(l):
            for j in range(s+1):
                if A[i] <= j:
                    dp[i+1][j] = max(dp[i][j], dp[i][j-A[i]] + A[i])
                else:
                    dp[i+1][j] = dp[i][j]
        return dp[l][m]
# 1d array
    def backPack(self,m,A):
        # write your code here
        n = len(A)
        dp = [0 for x in range(m+1)]
        dp[0] = 1
        ans = 0
        for item in A:
            for i in range(m,-1,-1):
                if i-item >=0 and dp[i-item] > 0:
                    ans = max(ans,i)
                    dp[i] = 1
        return ans    
