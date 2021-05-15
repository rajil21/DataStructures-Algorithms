



class Solution:
    def trappingWater(self, arr,n):
        #Code here
        L1=[0 for i in range(n)]
        L2=[0 for i in range(n)]
        L1[0]=arr[0]
        L2[-1]=arr[-1]
        for i in range(1,n):
            L1[i]=max(L1[i-1],arr[i-1])
        for i in range(n-2,-1,-1):
            L2[i]=max(arr[i+1],L2[i+1])
        c=0
        for i in range(1,n-1):
            if(min(L1[i],L2[i])-arr[i]>0):
                c+=min(L1[i],L2[i])-arr[i] 
        return c

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends