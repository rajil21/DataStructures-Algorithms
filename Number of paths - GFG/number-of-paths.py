#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        # print(a)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(i==1):
                    dp[i][j]=1
                elif(j==1):
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n][m]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)




# } Driver Code Ends