class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        A = lambda a,b:-1 if a+b > b+a else 1 if a+b < b+a else 0
        return str(int("".join(sorted(map(str,nums),key = cmp_to_key(A)))))
    
        