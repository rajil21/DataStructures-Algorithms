#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,a, n):
        
        #arr : given array
        #n : size of the array
        d={}
        for i in range(n):
            if(a[i] not in d):
                d[a[i]]=i
            else:
                return d[a[i]]+1
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends