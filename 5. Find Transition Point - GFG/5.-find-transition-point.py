def transitionPoint(A,n):
    #Code here
    i=0
    j=n-1
    while(i<=j):
        mid = (i+j)//2
        if(A[mid]==1 and A[mid-1]==0):
            j = mid
            break
        elif(A[mid]==0):
            i=mid+1
        elif(A[mid]==1 and A[mid-1]==1):
            j=mid-1
    if(A[-1]==0):
         return -1
    if(j==-1):
        return 0
    return j
            

#{ 
#  Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends