#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        # print(a)
        if(m==1 and n==1):
            return 1
        if(m==0 or n==0):
            return 0
        return Solution().numberOfPaths(m-1,n)+Solution().numberOfPaths(m,n-1)
        # code here


#{ 
#  Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)




# } Driver Code Ends