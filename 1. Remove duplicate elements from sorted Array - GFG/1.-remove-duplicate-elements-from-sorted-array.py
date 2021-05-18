#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code her
		i=1
		comp = A[0]
		for k in range(1,N):
		    if(comp!=A[k]):
		        A[i]=A[k]
		        comp = A[i]
		        i+=1
		return i 
		  
		  
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends