class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        d={}
        for i in nums:
            d[i]=0
        for i in nums:
            d[i]+=1
        ans=0
        if(k==0):
            for i in d:
                if(d[i]>1):
                    ans+=1
            return ans
        L=defaultdict(int)
        for i in d:
            ans+=L[i-k]+L[i+k]
            L[i]+=1
        return ans 