class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        pair={}
        t_set =set()
        for i in range(len(s)):
            if s[i] not in pair:
                if(t[i] in t_set):
                    return False
                pair[s[i]]=t[i]
                t_set.add(t[i])
            else:
                if( t[i]!=pair[s[i]]):
                    return False
        return True
            
            
        