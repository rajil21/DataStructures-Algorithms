#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, A, N, K):
		# code here
		def reverse(A,i,j):
		    while(i<j):
		        A[i],A[j]=A[j],A[i]
		        i+=1
		        j-=1
		for i in range(0,N,K):
		    if(i+K<N):
		        reverse(A,i,i+K-1)
		    else:
		        reverse(A,i,N-1)
		
#{ 
#  Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends