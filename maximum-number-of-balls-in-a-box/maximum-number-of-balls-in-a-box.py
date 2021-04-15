class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d={}
        for i in range(1,10**5+1):
            d[i]=0
        for i in range(lowLimit, highLimit+1):
            a = sum(list(map(int,str(i))))
            d[a]+=1
        return max(d.values())
        