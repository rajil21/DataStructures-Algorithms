class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxi = arr.index(max(arr))
        if(len(arr)<3):
            return False
        if(maxi==0 or maxi==len(arr)-1):
            return False
        for i in range(maxi):
            if(arr[i]>=arr[i+1]):
                return False
        for i in range(maxi,len(arr)-1):
            if(arr[i]<=arr[i+1]):
                return False
        return True
        