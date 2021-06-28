#User function Template for python3

# A[] : the input array of positive integers
# N : size of the array arr[]
# X : the required sum
class Solution:
    def keypair(self,A, N, X):
        # code here
        d={}
        for i in range(N):
            if(X-A[i] in d):
                return True
            else:
                d[A[i]]=i
        return False
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n,x=list(map(int,input().split()))
    a=list(map(int,input().split()))
    sln=Solution().keypair(a,n,x)
    if(sln):
        print("Yes")
    else:
        print("No")
# } Driver Code Ends