#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # code here
        if(n==1 or n==2):
            return n
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        M = 10**9 + 7
        for i in range(2,n):
            dp[i]=(dp[i-1]+dp[i-2])%M
        return dp[-1]%M
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(200000)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends