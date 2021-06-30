

class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        d={}
        for i in range(N):
            d[A[i]]=0
        c=0
        L=[]
        for i in range(K):
            if(d[A[i]]==0):
                c+=1
            d[A[i]]+=1
        L.append(c)
        for i in range(K,N):
            if(d[A[i-K]]==1):
                c-=1
            d[A[i-K]]-=1
            if(d[A[i]]==0):
                c+=1
            d[A[i]]+=1
            L.append(c)
        return L
            

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends