class Solution:
	def topK(self, a, k):
		#Code here
		n=len(a)
		d={}
        for i in range(n):
            d[a[i]]=0
        for i in range(n):
            d[a[i]]+=1
        d = sorted(d.items(),key= lambda x:(-x[1],-x[0]))
        L=[]
        for i in range(k):
            L.append(d[i][0])
        return L
        

#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends