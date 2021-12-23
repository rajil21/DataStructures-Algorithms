class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n = len(nums)
        def backtrack(prev,paths):
            if(len(prev)==n):
                result.append(list(prev))
                return
            for i in range(len(paths)):
                prev+=paths[i],
                backtrack(prev,(paths[:i]+paths[(i+1):]))
                prev.pop()
        backtrack([],nums)
        return result
                