class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        ans=0
        less = defaultdict(int)
        great = defaultdict(int)
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[i] <rating[j] :
                    less[i]+=1
                elif rating[i] > rating[j]:
                    great[i]+=1
        for i in range(len(rating)):
            for j in range(i+1,len(rating)):
                if rating[i] < rating[j] :
                    ans+=less[j]
                elif rating[i] > rating[j]:
                    ans+=great[j]       
        return ans
                    
                