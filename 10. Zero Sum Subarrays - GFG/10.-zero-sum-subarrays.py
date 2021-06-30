#User function Template for python3

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        d={}
        d[0]=1
        s=0
        c=0
        for i in range(n):
            s+=arr[i]
            if(s in d):
                c+=d[s]
                d[s]+=1
            else:
                d[s]=1
        return c
            
        
        #return: count of sub-arrays having their sum equal to 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
        
if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        A = [int(x) for x in input().strip().split(' ')]
        ob = Solution()
        print(ob.findSubArrays(A,N))
        
                
                
# } Driver Code Ends