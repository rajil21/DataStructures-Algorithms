class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        c=0
        L=[[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            L[i][0]=matrix[i][0]
            c+=L[i][0]
        for j in range(1,n):
            L[0][j]=matrix[0][j]
            c+=L[0][j]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==1:
                    L[i][j]=1+min(L[i-1][j],L[i][j-1],L[i-1][j-1])
                    c+=L[i][j]
                else:
                    L[i][j]=0
        return c