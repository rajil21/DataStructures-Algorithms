class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        m = (2**maximumBit)-1
        ans = []
        t = 0
        for i in range(len(nums)):
            t^=nums[i]
        while(len(nums)>0):
            ans.append(t^m)
            t^=nums.pop()
        return ans