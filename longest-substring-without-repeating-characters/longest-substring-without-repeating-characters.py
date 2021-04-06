class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L=[]
        l=""
        if(s==''):
            return 0
        for ch in s:
            if ch not in l:
                l+=ch
            else:
                L.append(len(l))
                l=l[l.index(ch)+1:]+ch
        L.append(len(l))
        return max(L)
            
                
        