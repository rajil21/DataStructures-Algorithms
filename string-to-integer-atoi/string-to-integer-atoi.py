class Solution:
    def myAtoi(self, s: str) -> int:
        a=''
        s = s.strip()
        k=0
        if(len(s)==0):
            return 0
        if(s[0]=='+' or s[0]=='-'):
            a+=s[0]
            k=1
        for i in range(k,len(s)):
            if(s[i].isnumeric()):
                a+=s[i]
            else:
                break
        if(a=='+' or a=='-' ):
            return 0
        if(len(a)==0):
            return 0
        b= int(a)
        if(b>2**31-1):
            return 2**31-1
        elif(b<-2**31):
            return -2**31
        return int(a)
        