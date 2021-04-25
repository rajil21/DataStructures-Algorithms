class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            d[i]=0
        for i in arr:
            d[i]+=1
        L=[]
        for i in d:
            if(d[i] not in L):
                L.append(d[i])
            else:
                return False
        return True