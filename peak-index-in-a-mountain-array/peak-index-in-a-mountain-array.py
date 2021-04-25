class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        L=[]
        for i in range(len(arr)-1):
            if(arr[i]<arr[i+1]):
                L.append(0)
            elif(arr[i]>arr[i+1]):
                L.append(1)
        ans =0
        c=0
        for i in range(len(L)-1):
            if(L[i]==0 and L[i+1]==1):
                c+=1
                ans = i+1
        if(c==1):
            return ans
        