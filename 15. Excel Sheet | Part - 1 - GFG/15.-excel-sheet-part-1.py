#User function Template for python3

class Solution:
    def ExcelColumn(self, n):
        #return required string
        #code here
        s=''
        L="ZABCDEFGHIJKLMNOPQRSTUVWXY"
        while(n>0):
            if(n%26==0):
                s+='Z'
                n=n//26-1
            else:
                s+=L[n%26]
                n//=26
        return s[::-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        ob=Solution()
        print(ob.ExcelColumn(n))

# } Driver Code Ends