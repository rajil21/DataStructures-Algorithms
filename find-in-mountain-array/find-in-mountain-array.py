# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        s = -2**31
        n  = mountain_arr.length()
        P,H=0,n-1
        while(P<H):
            mid = (H+P)//2
            if(mountain_arr.get(mid)<mountain_arr.get(mid+1)):
                P = mid+1
            else:
                H = mid
        l,h=0,P
        L=[]
        while l<=h:
            mid = (h+l)//2
            M = mountain_arr.get(mid)
            if(M>target):
                h = mid-1
            elif(M<target):
                l = mid+1
            elif(M==target):
                L.append(mid)
                break
        if(len(L)!=0):
            return L[0]
        l,h = P,n-1
        while l<=h:
            mid = (h+l)//2
            M = mountain_arr.get(mid)
            if(M<target):
                h = mid-1
            elif(M>target):
                l = mid+1
            elif(M==target):
                L.append(mid)
                break
        if(len(L)==0):
            return -1
        return min(L)