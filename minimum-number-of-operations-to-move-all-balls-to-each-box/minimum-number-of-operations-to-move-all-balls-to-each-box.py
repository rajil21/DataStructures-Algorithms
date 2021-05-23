class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        L=[0 for i in range(len(boxes))]
        for i in range(len(boxes)):
            c=0
            for j in range(len(boxes)):
                if(boxes[j]=='1'):
                    c+= abs(j-i)
            L[i]=c
        return L
            