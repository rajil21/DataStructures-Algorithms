#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    # code here
    i,j,c,ans=0,0,0,0
    while(i<n):
        if(arr[i]==0):
            c+=1
        while(c>m):
            if(arr[j]==0):
                c-=1
            j+=1
        ans  =max(ans,i-j+1)
        i+=1
    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends