#User function Template for python3

class Solution:
    def immediateSmaller(self,a,n,x):
        #return required ans
        m = 2**31
        ans=-1
        for i in range(n):
            if(x-a[i]>0 and x-a[i]<m):
                m=x-a[i]
                ans=a[i]
        return ans
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ =='__main__':
    tcs=int(input())
    
    for _ in range(tcs):
        n=int(input())
        arr=[int(e) for e in input().split()]
        x=int(input())
        ob=Solution()
        ans=ob.immediateSmaller(arr,n,x)
        print(ans)
# } Driver Code Ends