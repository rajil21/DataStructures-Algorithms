#User function Template for python3

class Solution:
    def reverseBits(self,n):
        #code here
        s=""
        while(n>0):
            s+=str(n%2)
            n=n//2
        c,l=0,0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=='1'):
                c+=2**l
            l+=1
        return c
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        ob=Solution()
        print(ob.reverseBits(n))
     
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends