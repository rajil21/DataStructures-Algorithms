class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n
        while ( l<r):
            m = (l+r)//2
            if(nums[m]==target):
                return m
            if(nums[m]<target):
                l = m+1
            else:
                r=m
        return l
        