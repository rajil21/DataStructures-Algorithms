# function to return maximum XOR subset in set[]

class Solution:
    def maxSubarrayXOR(self, arr, n):
        # add code here
        ind=0
        for i in range(31,-1,-1):
            ME=-2**31
            MI=ind
            for j in range(ind,n):
                if((arr[j]&(1<<i)!=0) and arr[j]>ME):
                    ME=arr[j]
                    MI=j
            if(ME==-2**31):
                continue
            arr[ind],arr[MI]=arr[MI],arr[ind]
            MI=ind
            for j in range(n):
                if(j!=MI and ((1<<i)&arr[j]!=0)):
                    arr[j]^=arr[MI]
            ind+=1
        ans=0
        for i in range(n):
            ans^=arr[i]
        return ans
        

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        set=list(map(int,input().split()))
        obj = Solution()
        print(obj.maxSubarrayXOR(set,n))
# } Driver Code Ends