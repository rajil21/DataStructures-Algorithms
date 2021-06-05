

#User function Template for python3

class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        #code here
        d={}
        for i in s:
            d[i]=0
        for i in s:
            d[i]+=1
        m=-2**31
        for i in d:
            if(d[i]>m):
                m = d[i]
                ans=i
            elif(d[i]==m and i<ans):
                ans=i
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(Solution().getMaxOccurringChar(s))
# } Driver Code Ends