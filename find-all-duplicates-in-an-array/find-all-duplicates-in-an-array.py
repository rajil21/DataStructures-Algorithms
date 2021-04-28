class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=0
        for i in nums:
            d[i]+=1
        L=[]
        for i in d:
            if(d[i]==2):
                L.append(i)
        return L
        