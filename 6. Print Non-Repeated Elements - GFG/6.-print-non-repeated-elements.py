
#User function Template for python3
class Solution:
    
    #Complete this function
    #Function to return non-repeated elements in the array.
    def printNonRepeated(self,arr,n):
        #Your code here
        d={}
        for i in range(n):
            d[arr[i]]=0
        for i in range(n):
            d[arr[i]]+=1
        L=[]
        for i in range(n):
            if(d[arr[i]]==1):
                L.append(arr[i])
        return L
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        l = Solution().printNonRepeated(arr,n)
        print(*l)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends