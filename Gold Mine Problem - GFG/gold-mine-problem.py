# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        # code here
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for j in range(m-1,-1,-1):
            for i in range(0,n):
                if(j==m-1):
                    dp[i][j]=M[i][j]
                elif(i==0):
                    dp[i][j]=M[i][j]+max(dp[i][j+1],dp[i+1][j+1])
                elif(i==n-1):
                    dp[i][j]=M[i][j]+max(dp[i][j+1],dp[i-1][j+1])
                else:
                    dp[i][j]=M[i][j]+max(dp[i][j+1],dp[i+1][j+1],dp[i-1][j+1])
        ans =0 
        for i in range(n):
            ans = max(ans,dp[i][0])
        return ans

#{ 
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends