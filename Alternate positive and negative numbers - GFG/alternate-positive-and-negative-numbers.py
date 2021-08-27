#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        L1=[]
        L2=[]
        for i in range(n):
            if(arr[i]>=0):
                L1.append(arr[i])
            else:
                L2.append(arr[i])
        j1=0
        j2=0
        i=0
        while(i<n and j1<len(L1) and j2<len(L2)):
            if(i%2==0):
                arr[i]=L1[j1]
                j1+=1
            else:
                arr[i]=L2[j2]
                j2+=1
            i+=1
        while(i<n and j1<len(L1)):
            arr[i]=L1[j1]
            i+=1
            j1+=1
        while(i<n and j2<len(L2)):
            arr[i]=L2[j2]
            i+=1
            j2+=1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends