

#User function Template for python3

class Solution:
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,mat,n):
        # code here 
        d=0
        if(len(mat)==1):
            return mat[0][0]
        elif(len(mat)==2):
            d = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
            return d
        else:
            for p in range(len(mat[0])):
                tempM = []
                for i in range(1,len(mat)):
                    temp=[]
                    for j in range(len(mat[0])):
                        if(j!=p):
                            temp.append(mat[i][j])
                    if(len(temp)>0):
                        tempM.append(temp)
                d+=mat[0][p]*pow(-1,p)*Solution().determinantOfMatrix(tempM,len(mat))
        return d

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends