#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        d={}
        D={}
        for i in A:
            d[i]=0
        for i in B:
            D[i]=0
        for i in A:
            d[i]+=1
        for i in B:
            D[i]+=1
        for i in d:
            if(i not in D  or d[i]!=D[i]):
                return False
        return True
        #return: True or False
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends