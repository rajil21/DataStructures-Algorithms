#User function Template for python3

class Solution:
    def trailingZeroes(self, N):
    	#code here 
    	l=1
    	c=0
    	while(N//(5**l)>0):
    	    c+=N//(5**l)
    	    l+=1
    	return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input()) 
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)
# } Driver Code Ends