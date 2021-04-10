class Solution:
    def finalPrices(self, A: List[int]) -> List[int]:
        n = len(A)
        for i in range(n-1):
            for j in range(i+1,n):
                if(A[j]<=A[i]):
                    A[i]=A[i]-A[j]
                    break
        return A
        