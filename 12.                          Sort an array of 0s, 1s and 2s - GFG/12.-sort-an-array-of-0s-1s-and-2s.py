#User function Template for python3

class Solution:
    def sort012(self,a,n):
        # code here
        l=0
        h=n-1
        m=0
        while(m<=h):
            if(a[m]==0):
                a[l],a[m]=a[m],a[l]
                m+=1
                l+=1
            elif(a[m]==1):
                m+=1
            else:
                a[m],a[h]=a[h],a[m]
                h-=1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends