class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        L=[]
        n = len(s)
        k = len(part)
        for i in range(n):
            if(len(L)>=k and "".join(L[len(L)-k:])==part):
                for _ in range(k):
                    L.pop()
                L.append(s[i])
            else:
                L.append(s[i])
        if(len(L)>=k and "".join(L[len(L)-k:])==part):
            for _ in range(k):
                L.pop()
        return "".join(L)