

#User function Template for python3

class Solution:
    
    #Function to find transpose of a matrix.
    def transpose(self,A, n):
        # code here 
        for i in range(n-1):
            for j in range(i+1,n):
                A[i][j],A[j][i] = A[j][i],A[i][j]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        obj.transpose(matrix,n)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end=" ")
        print()
            

# } Driver Code Ends