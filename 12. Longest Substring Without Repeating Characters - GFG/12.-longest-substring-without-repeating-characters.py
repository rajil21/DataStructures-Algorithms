#User function Template for python3

class Solution:
    def SubsequenceLength(self, s):
        #Codee here
        l = ''
        L=[]
        if(len(s)==''):
            return 0
        for i in s:
            if(i not in l):
                l+=i
            else:
                L.append(len(l))
                l=l[l.index(i)+1:]+i
        L.append(len(l))
        return max(L)

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    s = input()
    print(Solution().SubsequenceLength(s))
    
# } Driver Code Ends