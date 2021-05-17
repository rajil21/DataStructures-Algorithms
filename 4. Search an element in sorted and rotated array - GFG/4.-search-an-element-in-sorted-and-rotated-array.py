#User function Template for python3

def Search(arr,n,k):
    # #code here
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        l,m,h = arr[low],arr[mid],arr[high]
        if(arr[mid]==k):
            return mid
        elif(l<=k<m or(l>m and not(m<k<=h)) ):
            high=mid-1
        else:
            low=mid+1
    return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(Search(arr,n,k))

# } Driver Code Ends