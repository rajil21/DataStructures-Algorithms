class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c= defaultdict(list)
        for i,n in enumerate(nums):
            c[n].append(i)
        degree = max([len(x) for x in c.values()])
        result = len(nums)
        for i in c.values():
            if(len(i)==degree):
                result = min(result,i[-1]-i[0])
        return result+1
                