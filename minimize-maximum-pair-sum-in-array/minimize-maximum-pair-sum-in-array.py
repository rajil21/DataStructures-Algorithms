class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n,o  = len(nums),0
        nums.sort()
        for i in range(n//2):
            o = max(nums[i]+nums[n-i-1],o)
        return o
        