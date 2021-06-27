class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr, n):
        # Code here
        d={}
        for i in range(n):
            d[arr[i]]=[]
        for i in range(n):
            d[arr[i]].append(i)
        M=-2**31
        for i in d:
            M=max(-d[i][0]+d[i][-1],M)
        return M
            
        


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.maxDistance(arr, n))
# Contrbuted By:Harshit Sidhwa


# } Driver Code Ends