#User function Template for python3
class Solution:
    def search(self, A, N):
        # your code here
        c=0
        for i in range(N):
            c^=A[i]
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends