#User function Template for python3

class Solution:
    def sort012(self,a,arr_size):
        # code here
        lo = 0
    	hi = arr_size - 1
    	mid = 0
    	while mid <= hi:
    		if a[mid] == 0:
    			a[lo], a[mid] = a[mid], a[lo]
    			lo = lo + 1
    			mid = mid + 1
    		elif a[mid] == 1:
    			mid = mid + 1
    		else:
    			a[mid], a[hi] = a[hi], a[mid]
    			hi = hi - 1

                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends