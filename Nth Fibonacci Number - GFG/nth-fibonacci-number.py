#User function Template for python3
class Solution:
    def nthFibonacci (ob, n):
        # code here 
        if(n==1 or n==2):
            return 1
        L=[1,1]
        for i in range(2,n):
            L.append(L[-1]+L[-2])
        return L[-1]%((10**9)+7)

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends