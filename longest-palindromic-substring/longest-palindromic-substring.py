class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        ans = ''
        for i in range(L):
            for a, b in [(i,i), (i,i+1)]:
                while a>=0 and b < L and s[a]==s[b]:
                    a -= 1
                    b += 1
                if len(s[a+1:b])> len(ans):
                    ans=s[a+1:b]
        return ans
                    