#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # code here
        M=10**9+7
        if(n==1 or n==2):
            return n
        L=[0 for i in range(n+1)]
        L[1]=1
        L[2]=2
        for i in range(3,n+1):
            L[i]=L[i-1]+L[i-2]
        return L[n]%M

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends