class Solution:
    def trap(self, L: List[int]) -> int:
        c=0
        L1=[]
        L2=[]
        for i in range(len(L)):
            L1.append(L[i])
            L2.append(L[i])
        for i in range(1,len(L)):
            L1[i]=max(L1[i],L1[i-1])
        for i in range(len(L)-2,-1,-1):
            L2[i]=max(L2[i],L2[i+1])
        for i in range(1,len(L)-1):
            f=min(L1[i-1],L2[i+1])-L[i]
            if(f>0):
                c+=f            
        return c
        
        