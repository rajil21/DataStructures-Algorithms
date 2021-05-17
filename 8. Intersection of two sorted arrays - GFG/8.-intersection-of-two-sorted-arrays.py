#User function Template for python3

class Solution:
    #Function to return a list containing the intersection of two arrays.
    def printIntersection(self,a, b, n, m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return: array of intersection of two array or -1
        '''
        # code here
        L=[]
        i=0
        j=0
        while(i<n and j<m):
            if(a[i]==b[j]):
                L.append(a[i])
                i+=1
                j+=1
            elif(a[i]>b[j]):
                j+=1
            elif(b[j]>a[i]):
                i+=1
        if(len(L)==0):
            return [-1]
        for i in range(len(L)-1):
            if(L[i]==L[i+1]):
                L[i+1]=-1
        A=[]
        for i in L:
            if(i>0):
                A.append(i)
        return A

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        l = ob.printIntersection(a,b,n,m)
        print(*l)
# } Driver Code Ends