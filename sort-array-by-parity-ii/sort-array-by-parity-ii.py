class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        L1=[]
        L2=[]
        for i in A:
            if(i%2==0):
                L1.append(i)
            else:
                L2.append(i)
        for i in range(len(A)):
            if(i%2==0):
                A[i]=L1[i//2]
            else:
                A[i]=L2[i//2]
        return A
        