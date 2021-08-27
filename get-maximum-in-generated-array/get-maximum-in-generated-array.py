class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        L = [0,1]
        i=1
        while(len(L)<n+1):
            L.append(L[i])
            L.append(L[i]+L[i+1])
            i+=1
        return max(L[:-1]) if n%2==0 else max(L)