class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        if(s[0]=='-'):
            return False
        s=s[len(s)-1::-1]
        if(int(s)==x):
            return True
        else:
            return False
        