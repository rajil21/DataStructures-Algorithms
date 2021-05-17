#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
    #Your code here
        l =1
        h=x
        while(l<=h):
            m = (l+h)//2
            if(m*m==x):
                return m
            elif(m*m<x):
                l=m+1
                ans =m
            elif(m*m>x):
                h = m-1
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends