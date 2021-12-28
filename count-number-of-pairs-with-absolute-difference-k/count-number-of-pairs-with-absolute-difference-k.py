class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        L=defaultdict(int)
        ans = 0 
        for i in nums:
            ans+=L[i-k]+L[i+k]
            L[i]+=1
        return ans