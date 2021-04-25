class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        s=[]
        for i in range(m+1):
            t=[]
            for j in range(n+1):
                t.append(0)
            s.append(t)
        for i in range(1,m+1):
            for j in range(1,n+1):
                s[i][j] = mat[i-1][j-1]+s[i-1][j]+s[i][j-1]-s[i-1][j-1]
                # if(i-1<m and i>0):
                #     s[i][j]+=s[i-1][j]
                # if(j-1<n and j>0):
                #     s[i][j]+=s[i][j-1]
                # if(i-1<m and j-1<n and i>0 and j>0):
                #     s[i][j]-=s[i-1][j-1]
        a=[]
        for i in range(m):
            t=[]
            for j in range(n):
                t.append(0)
            a.append(t)
        for r in range(m):
            for c in range(n):
                r1,c1,r2,c2 = max(0,r-k),max(0,c-k),min(r+k,m-1),min(c+k,n-1)
                r1+=1
                c1+=1
                r2+=1
                c2+=1
                a[r][c] = s[r2][c2]-s[r2][c1-1]-s[r1-1][c2]+s[r1-1][c1-1]
        return a