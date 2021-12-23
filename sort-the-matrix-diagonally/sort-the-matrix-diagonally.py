class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d,m,n={},len(mat),len(mat[0])
        for i in range(m):
            for j in range(n):
                if (i-j not in d):
                    d[i-j]=[]
                d[i-j].append(mat[i][j])
        for i in d:
            d[i].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j]=d[i-j].pop()
        return mat