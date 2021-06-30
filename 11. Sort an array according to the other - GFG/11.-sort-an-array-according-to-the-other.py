#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        # Your Code Here
        d={}
        for i in range(N):
            d[A1[i]]=0
        for i in range(N):
            d[A1[i]]+=1
        L=[]
        for i in range(M):
            while(d[A2[i]]>0):
                L.append(A2[i])
                d[A2[i]]-=1
        l=[]
        # print(L)
        for i in range(N):
            if(A1[i] not in A2):
                l.append(A1[i])
        l.sort()
        # print(l)
        L.extend(l)
        return L
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends