#User function Template for python3

class Solution:
    
    ##Complete this function
    #Function to swap odd and even bits.
    def swapBits(self,n):
        #Your code here
        e = n&0xAAAAAAAA
        o = n&0x55555555
        e>>=1
        o<<=1
        return (e|o)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        print(ob.swapBits(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends