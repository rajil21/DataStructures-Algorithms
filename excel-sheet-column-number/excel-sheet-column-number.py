class Solution:
    def titleToNumber(self, s: str) -> int:
        c=0
        d={}
        p=1
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            d[i]=p
            p+=1
        l=0
        for i in range(len(s)-1,-1,-1):
            c+=(26**l)*d[s[i]]
            l+=1
        return c
        