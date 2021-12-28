class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans =[[]]
        for num in nums:
            ans+=[i+[num] for i in ans]
        return ans
            