class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        if(satisfaction[0]<1):
            return 0
        ans=0
        m=0
        for i in range(len(satisfaction)):
            m+=satisfaction[i]
            if(m>0):
                ans+=m
            else:
                return ans
        return ans
            