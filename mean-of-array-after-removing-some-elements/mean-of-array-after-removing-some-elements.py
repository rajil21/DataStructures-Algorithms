class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        c=0
        s=0
        for i in range(int(0.05*n),n-int(0.05*n)):
            s+=arr[i]
            c+=1
        return s/c
        