#User function Template for python3

def Search(arr,n,k):
    for i in range(n):
        if(arr[i]==k):
            return i
    return -1
    # #code here
    # l = 0
    # h = n-1
    # peak=-1
    # while(l<=h):
    #     mid = (l+h)//2
    #     if((mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1])):
    #         peak =mid
    #         break
    #     elif(mid>0 and arr[mid]<arr[mid-1]):
    #         h=mid-1
    #     elif(mid<n-1 and arr[mid]<arr[mid+1]):
    #         l=mid+1
    # l = 0 
    # h = peak
    # while(l<=h):
    #     mid = (l+h)//2
    #     if(arr[mid]==k):
    #         return mid
    #     elif(arr[mid]>k):
    #         h= mid-1
    #     elif(arr[mid]<k):
    #         l=mid+1
    # l = peak+1
    # h= n-1
    # while(l<=h):
    #     mid = (l+h)//2
    #     if(arr[mid]==k):
    #         return mid
    #     elif(arr[mid]>k):
    #         h= mid-1
    #     elif(arr[mid]<k):
    #         l=mid+1
    # return -1
    

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