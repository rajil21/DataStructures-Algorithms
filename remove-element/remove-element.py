class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = 51
                c+=1
        nums.sort()
        k = len(nums) - c
        return k