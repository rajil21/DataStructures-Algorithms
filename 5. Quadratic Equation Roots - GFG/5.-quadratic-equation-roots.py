#User function Template for python3
import math
class Solution:
	def quadraticRoots(self, a, b, c):
        # code here
        L=[]
        if(b*b<4*a*c):
            L.append(-1)
        else:
            L.append(int((-b+math.sqrt(b*b-4*a*c))//(2*a)))
            L.append(int((-b-math.sqrt(b*b-4*a*c))//(2*a)))
            if(L[0]<L[1]):
                L[0],L[1]=L[1],L[0]
        return L



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a,b,c)
        if len(ans)==1 and ans[0]==-1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()

# } Driver Code Ends