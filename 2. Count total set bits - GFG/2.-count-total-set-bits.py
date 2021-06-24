#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        n = n+1
        c=  n//2
        pi = 2
        while(pi<=n):
            tp = n//pi
            c+=(tp//2)*pi
            if(tp%2==1):
                c+=n%pi
            pi<<=1
        return c
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends