class Solution:
    def canJump(self, A: List[int]) -> bool:
        n = len(A)
        j = n-1
        for i in range(n-2,-1,-1):
            if(i+A[i]>=j):
                j=i
        if(j==0):
            return True
        return False
        