class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if(j==0 or i==0):
                    dp[i][j]=int(matrix[i][j])
        for i in range(1,m):
            for j in range(1,n):
                if(matrix[i][j]=='1'):
                    dp[i][j]=1+ min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        ans =0 
        for i in range(m):
            for j in range(n):
                ans = max(ans,dp[i][j])
        return ans*ans
        