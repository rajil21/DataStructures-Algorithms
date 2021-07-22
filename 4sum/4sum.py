class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        L=set()
        nums.sort()
        if(len(nums)<4):
            return []
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                k=j+1
                l=len(nums)-1
                while(k<l):
                    if(nums[i]+nums[j]==target-nums[k]-nums[l]):
                        L.add((nums[i],nums[j],nums[k],nums[l]))
                        k+=1
                        l-=1
                    elif(nums[i]+nums[j]>target-nums[k]-nums[l]):
                        l-=1
                    else:
                        k+=1
        return L
        