class Solution:
    def reverse(self, x: int) -> int:
        s= str(x)
        if(s[0]=='-'):
            s="-"+s[len(s)-1:0:-1]
        else:
            s =s[len(s)-1::-1]
        if(x>=0):
            if(x > 2**31-1 or int(s) >2**31-1 ):
                return 0
        else:
            if(abs(x) > 2**31 or abs(int(s))>2**31-1 ):
                return 0
        return int(s)
        