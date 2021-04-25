class Solution:
    def numberOfMatches(self, n: int) -> int:
        m =n
        a = n 
        s=0
        while(a!=1):
            if(m%2==0):
                a=(m//2)
                m=(m//2)
            else:
                a = (m-1)//2+1
                m=(m-1)//2
            s+=m
            m=a
        return s