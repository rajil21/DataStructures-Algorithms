class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        c=0
        for i in range(len(s)):
            for j in range(len(t)):
                p,q=i,j
                temp =0
                while(p<len(s) and q<len(t)):
                    if(s[p]!=t[q]):
                        temp+=1
                        if(temp>1):
                            break
                    p+=1
                    q+=1
                    if(temp==1):
                        c+=1
        return c