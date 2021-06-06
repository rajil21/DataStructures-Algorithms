class Solution:
    def minOperations(self, a: str) -> List[int]:
        l,r,prev=0,0,0
        n = len(a)
        for i in range(n):
            if(a[i]=='1'):
                r+=1
                prev+=i+1
        L=[0 for i in range(n)]
        for i in range(n):
            L[i] = prev + l-r
            if(a[i]=='1'):
                l+=1
                r-=1
            prev = L[i]
        return L
            