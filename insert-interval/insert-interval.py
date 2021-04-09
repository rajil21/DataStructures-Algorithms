class Solution:
    def insert(self, a: List[List[int]], b: List[int]) -> List[List[int]]:
        L=[]
        i=-1
        for i, (x,y) in enumerate(a):
            if(b[0]>y):
                L.append([x,y])
            elif( b[1]<x):
                i-=1
                break
            else:
                b[0] = min(b[0],x)
                b[1]=max(b[1],y)
        return L + [b]+ a[i+1:]
        