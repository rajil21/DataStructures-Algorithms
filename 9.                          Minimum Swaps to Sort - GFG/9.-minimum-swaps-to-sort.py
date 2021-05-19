


class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
	    c=0
	    temp = nums.copy()
	    d={}
	    temp.sort()
	    for i in range(n):
	        d[nums[i]]=i
	    init = 0
	    for i in range(n):
	        if(nums[i]!=temp[i]):
	            c+=1
	            init = nums[i]
	            nums[i],nums[d[temp[i]]]=nums[d[temp[i]]],nums[i]
	            d[init] = d[temp[i]]
	            d[temp[i]]=i
	    return c

#{ 
#  Driver Code Starts



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends