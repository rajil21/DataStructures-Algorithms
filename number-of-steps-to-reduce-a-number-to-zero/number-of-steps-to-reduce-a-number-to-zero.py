class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = num
        c=0
        while(n>0):
            c+=1
            if(n%2):
                n-=1
            else:
                n=n//2
        return c