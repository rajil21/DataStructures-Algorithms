#User function Template for python3

class Solution:
    def findNth(self,N):
        #code here
        ans=0
        i=0
        while(N):
            ans+=(10**i)*(N%9)
            N=N//9
            i+=1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
# } Driver Code Ends