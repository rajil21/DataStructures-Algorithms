class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in nums1:
            d[i]=0
        for i in nums1:
            d[i]+=1
        L=[]
        for i in d:
            if i in nums2:
                L.append(i)
        return L
        