

#User function Template for python3

class Solution:
    
    #Function to multiply two matrices.
    def multiplyMatrix(self,A,B):
        # code here 
        m = len(A)
        n = len(A[0])
        m1 = len(B)
        n1 = len(B[0])
        
        if(n==m1):
            L= [[0 for i in range(n1)] for j in range(m)]
            for i in range(m):
                for j in range(n1):
                    for k in range(m1):
                        L[i][j]+= A[i][k]*B[k][j]
            return L
        return []


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1,m1 = map(int,input().strip().split())
        A = [[0 for j in range(m1)] for i in range(n1)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(n1):
            for j in range (m1):
                A[i][j]=line1[k]
                k+=1
       
        n2,m2 = map(int,input().strip().split())
        B = [[0 for j in range(m2)] for i in range(n2)]
        line2 = [int(x) for x in input().strip().split()]
        k=0
        for i in range(n2):
            for j in range (m2):
                B[i][j]=line2[k]
                k+=1
        obj = Solution()
        ans = obj.multiplyMatrix(A,B)

        if(len(ans) == 0):
            print(-1)
        else:
            for i in range(len(ans)):
                for j in range (len(ans[0])):
                    print(ans[i][j],end=' ')
            print() 

# } Driver Code Ends