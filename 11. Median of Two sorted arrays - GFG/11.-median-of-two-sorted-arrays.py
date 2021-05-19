#User function Template for python3

class Solution:
    
    #Function to find the median of the two arrays when they get merged.
    def findMedianSortedArrays(self,a, m, b, n):
        i=0
        j=0
        L=[]
        while(i<m and j<n):
            if(a[i]<=b[j]):
                L.append(a[i])
                i+=1
            else:
                L.append(b[j])
                j+=1
        while(i<m):
            L.append(a[i])
            i+=1
        while(j<n):
            L.append(b[j])
            j+=1
        if(len(L)%2):
            return L[len(L)//2]
        else:
            return (L[len(L)//2]+L[len(L)//2-1])//2
                
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n1,n2=list(map(int,(input().split())))
        arr1=list(map(int,(input().split())))
        arr2=list(map(int,(input().split())))
        
        if n1<n2:
            print(Solution().findMedianSortedArrays(arr1,n1, arr2,n2))
        else:
            print(Solution().findMedianSortedArrays(arr2,n2, arr1,n1))
# } Driver Code Ends