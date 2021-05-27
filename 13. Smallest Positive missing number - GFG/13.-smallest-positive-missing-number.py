#User function Template for python3

class Solution:
    def findMissing(self,arr, size): 
        # your code goes here
        L=[True for i in range(size)]
        for i in range(size):
            if(arr[i]>0 and arr[i]-1< size):
                L[arr[i]-1] =False
        for i in range(size):
            if(L[i]==True):
                return i+1
        return size+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.findMissing(arr, n))
# } Driver Code Ends