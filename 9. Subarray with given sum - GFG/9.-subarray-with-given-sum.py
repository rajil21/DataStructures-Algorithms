#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,a, n, s): 
        #Your code here
        for i in range(1,n):
            a[i]+=a[i-1]
        
        for i in range(n):
            if(a[i]==s):
                return [1,i+1]
        # print(a)
        i=0
        j=1
        while(j<n):
            if(a[j]-a[i]>s):
                i+=1
                # print("I=",i)
            elif(a[j]-a[i]<s):
                j+=1
                # print("J=",j)
            elif(a[j]-a[i]==s):
                return [i+2,j+1]
        return [-1]
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends