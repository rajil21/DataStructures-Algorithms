#User function Template for python3

class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        n1 = m-l+1
        n2 = r-m
        L=[]
        R=[]
        for i in range(n1):
            L.append(arr[i+l])
        for j in range(n2):
            R.append(arr[m+1+j])
        i=0
        j=0
        k=l
        while(i<n1 and j<n2):
            if(L[i]<=R[j]):
                arr[k]=L[i]
                i+=1
            elif(R[j]<L[i]):
                arr[k]=R[j]
                j+=1
            k+=1
        while(i<n1):
            arr[k]=L[i]
            i+=1
            k+=1
        while(j<n2):
            arr[k]=R[j]
            j+=1
            k+=1
    def mergeSort(self,arr, l, r):
        #code here
        if(l<r):
            m = (l+r)//2
            Solution().mergeSort(arr,l,m)
            Solution().mergeSort(arr,m+1,r)
            Solution().merge(arr,l,m,r)


#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends