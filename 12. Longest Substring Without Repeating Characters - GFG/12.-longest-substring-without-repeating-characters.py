#User function Template for python3

class Solution:
    def SubsequenceLength(self, s):
        #Codee here
        m = -2**31
        i,j=0,0
        if(len(s)==0):
            return 0
        d={}
        for p in "abcdefghijklmnopqrstuvwxyz":
            d[p]=0
        while(j<len(s)):
            if(d[s[j]]!=0):
                d[s[i]]=0
                i+=1
            else:
                d[s[j]]=1
                m = max(m,j-i+1)
                j+=1
        
        return m
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    s = input()
    print(Solution().SubsequenceLength(s))
    
# } Driver Code Ends