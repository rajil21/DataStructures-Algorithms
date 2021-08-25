#User function Template for python3

class Solution:
    def canReach(self, A, N):
        # code here 
        j=N-1
        for i in range(N-2,-1,-1):
            if(i+A[i]>=j):
                j = i
        if(j==0):
            return 1
        return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.canReach(A,N))
# } Driver Code Ends