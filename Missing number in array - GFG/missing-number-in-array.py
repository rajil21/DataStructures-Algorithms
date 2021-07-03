#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        # code here
        ans=0
        for i in range(n):
            ans^=(i+1)
            if(i<n-1):
                ans^=array[i]
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends