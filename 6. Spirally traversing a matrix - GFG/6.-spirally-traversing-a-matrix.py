#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,m, r, c): 
        # code here 
        k=0 # Column 
        l=0  # row 
        L=[]
        while(l<r and k<c):
            for i in range(k,c):
                L.append(m[l][i])
            l+=1
            for i in range(l,r):
                L.append(m[i][c-1])
            c-=1
            if(l<r):
                for i in range(c-1,k-1,-1):
                    L.append(m[r-1][i])
                r-=1
            if(k<c):
                for i in range(r-1,l-1,-1):
                    L.append(m[i][k])
                k+=1
        return L
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends