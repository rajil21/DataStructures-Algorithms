class Solution(object):
    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        d=[]
        def ans(n):
            c=0
            while(n!=1):
                if(n%2):
                    n = 3*n+1
                else:
                    n = n//2
                c+=1
            return c
        for i in range(lo,hi+1):
            d.append([i,ans(i)])
        d.sort(key = lambda x:x[1])
        return d[k-1][0]
        
        